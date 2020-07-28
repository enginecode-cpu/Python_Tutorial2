# Chapter6-1
# 파이썬 심화
# 흐름 제어, 병행처리(Concurrency)
# 제너레이터, 반복형
# Generator

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, Unpacking, *args
# 공부할 것 : 반복형 객체 내부적으로 iter 함수 내용, 제너레이터 동작 원리, yield from

# 반복 가능한 이유 -> iter(x) 함수를 호출

t = "ABCDEF"

# for 사용
for c in t:
    print("Ex1-1 -", c)
print()

w = iter(t)

# while 사용
while 1:
    try:
        print("Ex1-2 -", next(w))
    except StopIteration:
        # print(log)
        break
print()

from collections import abc

# 반복형
print("Ex1-3 -", hasattr(t, "__iter__"))
print("Ex1-4 -", isinstance(t, abc.Iterable))
print()

# next 사용

class WordSplitIter(object):
    def __init__(self, text):
        self.idx = 0
        self.text = text.split(" ")

    def __next__(self):
        # print("Called __next__")
        try:
            word = self.text[self.idx]
        except IndexError:
            raise StopIteration()
        self.idx += 1
        return word
    
    def __iter__(self):
        print("Called __iter__")
        return self

    def __repr__(self):
        return "WordSplit(%s)" %(self.text)


wi = WordSplitIter("I am Python Programmer")

print("Ex2-1 -", wi)
print("Ex2-2 -", next(wi))
print("Ex2-3 -", next(wi))
print("Ex2-4 -", next(wi))
print("Ex2-4 -", next(wi))
# print("Ex2-6 -", next(wi)) # Error
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터셋이 증가될 경우 메모리 사용량이 증가 -> 제너레이터 완화
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3. 딕셔너리, 리스트 한 번 호출할 때마다 하나의 값만 리턴 -> 아주 작은 메모리 양을 필요로 한다.


class WordSplitGenerator(object):
    def __init__(self, text):
        self.text = text.split(" ")

    def __iter__(self):
        for word in self.text:
            yield word
        return

    def __repr__(self):
        return "WordSplit(%s)" %(self.text)

wg = WordSplitGenerator("I am Python Programmer")

wt = iter(wg)

print("Ex3-1 -", wt)
print("Ex3-2 -", next(wt))
print("Ex3-3 -", next(wt))
print("Ex3-4 -", next(wt))
print("Ex3-4 -", next(wt))
# print("Ex3-6 -", next(wt)) # Error
print()


# Generator 예제1
def generator_ex1():
    print("Start")
    yield "AAA"
    print("Continue")
    yield "BBB"
    print("End")

temp = iter(generator_ex1())

# print("Ex4-1 -", next(temp))
# print("Ex4-2 -", next(temp))
# print("Ex4-3 -", next(temp)) # Error

for v in generator_ex1():
    pass
    # print("Ex4-4 -", v)

# Generator 예제2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print("Ex5-1 -", temp2)
print("Ex5-2 -", temp3)

for i in temp2:
    print("Ex5-3 -", i)
print()

for i in temp3:
    print("Ex5-4 -", i)
print()

# Generator 예제3(자주 사용하는 함수)

import itertools

gen1 = itertools.count(1, 2.5)

print("Ex6-1 -", next(gen1))
print("Ex6-2 -", next(gen1))
print("Ex6-3 -", next(gen1))
print("Ex6-4 -", next(gen1))
print("Ex6-5 -", next(gen1))
# ... 무한
print()


# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print("Ex6-6 -", v)
print()


# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print("Ex6-7 -", v)
print()


# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print("Ex6-8 -", v)
print()


# 연결1
gen5 = itertools.chain("ABCDE", range(1, 11, 2))

print("Ex6-9 -", list(gen5))


# 연결2
gen6 = itertools.chain(enumerate("ABCDE"))

print("Ex6-10 -", list(gen6))


# 개별
gen7 = itertools.product("ABCDE")

print("Ex6-11 -", list(gen7))

# 연산(경우의 수)
gen8 = itertools.product("ABCDE", repeat=2)

print("Ex6-11 -", list(gen8))

# 그룹화
gen9 = itertools.groupby("AAABBCCCCDDEEEE")

# 개별
gen7 = itertools.product("ABCDE")

# print("Ex6-12 -", list(gen9))

for char, group in gen9:
    print("Ex6-12 -", char, ':', list(group))
print()