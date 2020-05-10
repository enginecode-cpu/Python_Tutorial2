# Chapter5-1
# 파이썬 심화
# 일급 함수(일급 객체)
# Decorator & Closure

# 파이썬 변수 범위(global)

# 예제1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(5) # Error

# 예제2
b = 10

def func_v2(a):
    print(a)
    print(b)

func_v2(5)

# 예제3
b = 10

def func_v3(a):
    print(a)
    print(b)
    b = 5

# func_v3(5)

from dis import dis

print("Ex1-1 -")
print(dis(func_v3))
print()

# Closure(클로저)
# 반환되는 내부 함수에 대해서 선언된 연결 정보를 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다

a = 10

print("Ex2-1 -", a + 10)
print("Ex2-2 -", a + 100)

# 결과를 누적할 수 없을까
print("Ex2-3 -", sum(range(1, 51)))
print("Ex2-4 -", sum(range(51, 101)))
print()


# 클래스 이용
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, v):
        self.series.append(v)
        print("Class >>> {} / {}".format(self.series, len(self.series)))
        return sum(self.series) / len(self.series)

# 인스턴스 생성
avg_cls = Averager()

# 누적 확인
print("Ex3-1 -", avg_cls(15))
print("Ex3-2 -", avg_cls(35))
print("Ex3-3 -", avg_cls(40))
print()

# 클로저 사용
# 전역 변수 사용 감소
# 디자인 패턴 적용
# 많이 사용할 경우에는 자원을 많이 잡아먹을 수 있다

def closure_avg1():
    # Free variable
    series = []
    # 클로저 영역
    def averager(v):
        # series = [] # 유지가 되지 않는다
        series.append(v)
        print("def1 >>> {} / {}".format(series, len(series)))
        return (sum(series) / len(series))
    return averager

avg_closure1 = closure_avg1()

print("Ex4-1 -", avg_closure1(15))
print("Ex4-2 -", avg_closure1(35))
print("Ex4-3 -", avg_closure1(40))
print()

print("Ex5-1 -", dir(avg_closure1))
print()
print("Ex5-2 -", dir(avg_closure1.__code__))
print()
print("Ex5-3 -", avg_closure1.__code__.co_freevars)
print()
print("Ex5-4 -", dir(avg_closure1.__closure__[0]))
print()
print("Ex5-5 -", dir(avg_closure1.__closure__[0].cell_contents))
print()

# 잘못된 클로저 사용 예
def closure_avg2():
    # Free variable
    cnt = 0
    total = 0
    # 클로저 영역
    def averager(v):
        nonlocal cnt, total # Free variable을 로컬에서도 사용할 것이라는 예약어
        cnt += 1
        total += v
        print("def2 >>> {} / {}".format(total, cnt))
        return total / cnt
    return averager

avg_closure2 = closure_avg2()

print("Ex5-5 -", avg_closure2(15))
print("Ex5-5 -", avg_closure2(35))
print("Ex5-5 -", avg_closure2(40))

# 데코레이터 실습
# 장점
# 1. 중복 제거, 코드 간결
# 2. 클로저보다 문법 간결
# 3. 조합해서 사용 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함
# 3. 에러 발생 지점 추적 어려움 -> IDE로 해결 가능

import time

def performance_clock(func):
    def perf_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st
        # 내가 실행한 함수명
        name = func.__name__
        # 매개 변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 출력
        print('Result : [%0.5fs] %s(%s) -> %r' %(et, name, arg_str, result))
        return result
    return perf_clocked

@performance_clock
def time_func(seconds):
    time.sleep(seconds)

@performance_clock
def sum_func(*numbers):
    return sum(numbers)

@performance_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)

# 데코레이터 미사용

non_deco1 = performance_clock(time_func)
non_deco2 = performance_clock(sum_func)
non_deco3 = performance_clock(fact_func)

print("Ex7-1 -", non_deco1, non_deco1.__code__.co_freevars)
print("Ex7-2 -", non_deco2, non_deco2.__code__.co_freevars)
print("Ex7-3 -", non_deco3, non_deco3.__code__.co_freevars)

print("*" * 40, "Called Non Deco -> time func")
print("Ex7-4 -")
non_deco1(2)
print("*" * 40, "Called Non Deco -> sum func")
print("Ex7-5 -")
non_deco2(100, 200, 300, 500)
print("*" * 40, "Called Non Deco -> fact func")
print("Ex7-6 -")
non_deco3(100)

print()

print("*" * 40, "Called Deco -> time func")
print("Ex7-7 -")
time_func(2)
print("*" * 40, "Called Deco -> sum func")
print("Ex7-8 -")
sum_func(10, 20, 30, 40, 50)
print("*" * 40, "Called Deco -> fact func")
print("Ex7-9 -")
# fact_func(100)
