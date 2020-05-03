# Chapter2-1
# 파이썬 심화
# 데이터 모델(Data Model)
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임 워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)

# 객체 - 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value
# 파이썬 -> 일관성

# 일반적인 튜플을 사용했을 경우
# 0 : x, 1 : y
from math import sqrt

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
line_len1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print("Ex1-1 - ", line_len1)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple("Point", 'x y')

# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# 계산
line_len2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

# 출력
print("Ex1-2 - ", line_len2)
print("Ex1-3 - ", line_len1 == line_len2)


# 네임드 튜플 선언 방법
Point1 = namedtuple("Point", ['x', 'y'])
Point2 = namedtuple("Point", 'x, y')
Point3 = namedtuple("Point", "x y")
Point4 = namedtuple("Point", "x y x class", rename=True) # Default=False

# 출력
print("Ex2-1 - ", Point1, Point2, Point3, Point4)
print()
# Dict to Unpacking
temp_dict = {'x':75, 'y':55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

# 출력
print("Ex2-2 - ", p1, p2, p3, p4, p5)
print()

# 사용
print("Ex3-1 - ", p1[0] + p2[1])
print("Ex3-2 - ", p1.x + p2.y) # 클래스 변수 접근 방식

# Unpacking
x, y = p3
print("Ex3-3 - ", x + y)

# Rename 테스트
print("Ex3-4 - ", p4)
print()

# 네임드 튜플 메소드

temp = [52, 38]

# _make() : 새로운 객체를 생성
p4 = Point1._make(temp)
print("Ex4-1 - ", p4)

# _fields : 필드 네임 확인
print("Ex4-2 - ", p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환 -> 정렬된 딕셔너리로 반환
print("Ex4-3 - ", p1._asdict(), p4._asdict())

# _replace() : 수정된 '새로운' 객체를 반환
print("Ex4-4 - ", p2._replace(y=100))
print()

# 실 사용 실습
# 학생 전체 그룹 생성
# 반 20명, 4개의 반 -> (A, B, C, D) 번호

# 네임드 튜플 선언
Classes = namedtuple("Classes", ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# 중간 확인
# print(numbers)
# print(rank, numbers)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print("Ex5-1 - ", students)
print("Ex5-2 - ", len(students))
print()

# 가독성이 안 좋은 경우
students2 = [Classes(rank, number) for rank in "A B C D".split() for number in [str(n) for n in range(1, 21)]]
print("Ex6-1 - ", students2)
print("Ex6-2 - ", len(students2))
print()

# 출력
for s in students:
    print("Ex7-1 - ", s)