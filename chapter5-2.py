# Chapter5-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class ABC

# Class 선언
class VectorP():
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y)) # Generator

    @property
    def x(self):
        print("Called Property X")
        return self.__x
    
    @x.setter
    def x(self, v):
        print("Called Property X Setter")
        self.__x = v

    @property
    def y(self):
        print("Called Property Y")
        return self.__y
    
    @y.setter
    def y(self, v):
        print("Called Property Y Setter")
        if v < 30:
            raise ValueError("30 below is impossible")
        self.__y = v


# 객체 선언
v = VectorP(20, 40)

# print("Ex1-1 -", v.x, v.y)

# Getter, Setter
print("Ex1-2 -", dir(v), v.__dict__)
print("Ex1-3 -", v.x, v.y)

# Iter 확인
for val in v:
    print("Ex1-3 -", val)


# __slot__
# 파이썬 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용

class TestA(object):
    __slots__ = ('a',)


class TestB(object):
    pass

use_slot = TestA()
no_slot = TestB()

print("Ex2-1 -", use_slot)
# print("Ex2-2 -", use_slot.__dict__) # Error

print("Ex2-3 -", no_slot)
print("Ex2-4 -", no_slot.__dict__)

# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner():
        obj.a = "TEST"
        del obj.a
    return repeat_inner

print(min(timeit.repeat(repeat_outer(use_slot), number=500000)))
print(min(timeit.repeat(repeat_outer(no_slot), number=500000)))
print()

# 객체 슬라이싱

class Objects(object):
    def __init__(self):
        self.numbers = [n for n in range(1, 10000, 3)]

    def __len__(self):
        return len(self.numbers)

    def __getitem__(self, idx):
        return self.numbers[idx]

s = Objects()

print("Ex3-1 -", s.__dict__)
print("Ex3-2 -", len(s))
print("Ex3-3 -", len(s.numbers))
print("Ex3-4 -", s[1:100])
print("Ex3-5 -", s[-1])
print("Ex3-6 -", s[::10])
print()

# 파이썬 추상 클래스

# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 인스턴스를 생성해야 한다.
# 추상 클래스를 사용하는 이유
# -> 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것

# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contain__ 기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜

class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]

i1 = IterTestA()

print("Ex4-1 -", i1[4])
print("Ex4-2 -", i1[4:10])
print("Ex4-3 -", 3 in i1[1:10])
print("Ex4-4 -", [i for i in i1])
print()

# Sequence 상속
# 요구 사항인 추상 메소드를 모두 구현해야 동작

from collections.abc import Sequence

class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])

i2 = IterTestB()
print("Ex4-5 -", i2[4])
print("Ex4-6 -", i2[4:10])
print("Ex4-7 -", 3 in i2[1:10])
print("Ex4-8 -", [i for i in i2])
print()

# abc 활용 예제
import abc

class Random_Machine(abc.ABC):
    # 추상 메소드
    @abc.abstractmethod
    def load(self, iterobj):
        """Iterable 항목 추가"""
    
    # 추상 메소드
    @abc.abstractmethod
    def pick(self, iterobj):
        """무작위 항목 뽑기"""

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))

import random

class Crane_Machine(Random_Machine):
    def __init__(self, items):
        self.randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self.randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("Empty Crane Box")

    def __call__(self):
        return self.pick()

# 서브 클래스 확인
print("Ex5-1 -", issubclass(Random_Machine, Crane_Machine))
print("Ex5-2 -", issubclass(Crane_Machine, Random_Machine))

print("Ex5-3 -", Crane_Machine.__mro__)

# 추상 메소드 오버라이딩 안 하면 에러
cm = Crane_Machine(range(1, 100))

print("Ex5-4 -", cm._items)
print("Ex5-5 -", cm.pick())
print("Ex5-6 -", cm())
print("Ex5-7 -", cm.inspect())