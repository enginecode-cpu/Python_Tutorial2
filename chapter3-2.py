# Chapter3-2
# 파이썬 심화
# 시퀀스형
# 해쉬 테이블 -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# Dict 구조
print("Ex1-1 -")
# print(__builtins__.__dict__)
print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print("Ex1-2 -", hash(t1))
# print("Ex1-3 -", hash(t2)) # List 때문에 Error 
print()

# 지능형 딕셔너리(Comprehension Dict)
import csv

# 외부 CSV to List of tuple
with open('./resources/test1.csv', 'r', encoding='utf-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print("Ex2-1 -")
print(NA_CODES)

n_codes1 = {country : code for country, code in NA_CODES}
n_codes2 = {country.upper() : code for country, code in NA_CODES}

print()

print("Ex2-2 -")
print(n_codes1)

print()

print("Ex2-3 -")
print(n_codes2)

print()

# Dict Setdefault 예제
source = (
    ('k1', 'val1'),
    ('k2', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5')
)

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print("Ex3-1 -", new_dict1)

# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print("Ex3-2 -", new_dict2)

# 사용자 정의 dict 상속(UseDict 가능)

class UserDict(dict):
    def __missing__(self, key):
        print("Called : __missing__")
        if isinstance(key, str):
            raise KeyError(key)
        return self[str[key]]

    def get(self, key, default=None):
        print("Called : __getitem__")
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        print("Called : __contains__")
        return key in self.keys() or str(key) in self.keys()

user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({"one" : 1, "two" : 2})
user_dict3 = UserDict([("one", 1), ("two", 2)])

# 출력
print("Ex4-1 -", user_dict1, user_dict2)
print("Ex4-2 -", user_dict2.get('two'))
print("Ex4-3 -", "one" in user_dict3)
# print("Ex4-4 -", user_dict3["three"]) # Error
print("Ex4-5 -", user_dict3.get("three"))
print("Ex4-6 -", "three" in user_dict3)
print()
# Immutable Dict

from types import MappingProxyType

d = {"key1" : "TEST1"}

# Read Only
d_frozen = MappingProxyType(d)

print("Ex5-1 -", d, id(d))
print("Ex5-2 -", d_frozen, id(d_frozen))
print("EX5-3 -", d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen["key2"] = "TEST2" # Error 

d["key2"] = "TEST2"

print("EX5-4 -", d)
print()

# Set 구조(FrozenSet)
s1 = {"Apple", "Orange", "Apple", "Orange", "Kiwi"}
s2 = set(["Apple", "Orange", "Apple", "Orange", "Kiwi"])
s3 = {3}
s4 = set()
s5 = frozenset()

# 추가
s1.add("Melon")

# 추가 불가
# s5.add("Melon") # Error
print("Ex6-1 -", s1, type(s1))
print("Ex6-2 -", s1, type(s2))
print("Ex6-3 -", s1, type(s3))
print("Ex6-4 -", s1, type(s4))
print("Ex6-5 -", s1, type(s5))
print()
# 선언 최적화
from dis import dis

print("Ex6-6 -")
print(dis('{10}'))
print("Ex6-7 -")
print(dis('set([10])'))

# 지능형 집합(Comprehension Set)
from unicodedata import name

print("Ex7-1 -")
print({chr(i)for i in range(0, 256)})
print({name(chr(i), '')for i in range(0, 256)})