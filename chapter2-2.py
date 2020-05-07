# Chapter2-2
# 파이썬 심화

# 매직메소드 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)

# 매직 메소드 기초 설명

# 기본형
print(int) # <class 'int'>

# 모든 속성 및 메소드 출력
print(dir(int))
print()
print()

n = 100

# 사용
print("Ex1-1 - ", n + 200) # Ex1-1 -  300
print("Ex1-2 - ", n.__add__(200)) # Ex1-2 -  300
print("Ex1-3 - ", n.__doc__)
print("Ex1-4 - ", n.__bool__()) # Ex1-4 -  True
print("Ex1-5 - ", n * 100, n.__mul__(100)) # Ex1-5 -  10000 10000
print()
print()

# 클래스 예제1
class Student():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return "Student Class Info : {}, {}".format(self.name, self.height)
    
    def __ge__(self, value):
        print("Called. >> __ge__ Method.")
        if self.height >= value.height:
            return True
        else:
            return False
        
    def __le__(self, value):
        print("Called. >> __le__ Method.")
        if self.height <= value.height:
            return True
        else:
            return False

    def __sub__(self, value):
        print("Called. >> __sub__ Method.")
        return self.height - value.height

# 인스턴스 생성
s1 = Student('Kim', 180)
s2 = Student("Lee", 165)

# 매직 메소드 출력
print("Ex2-1 - ", s1 >= s2)
print("Ex2-2 - ", s1 <= s2)

print("Ex2-3 - ", s1 - s2)
print("Ex2-4 - ", s2 - s1)
print("Ex2-5 - ", s1)
print("Ex2-6 - ", s2)
print()

# 클래스 예제2
# 벡터(Vector)
class Vector(object):
    def __init__(self, *args):
        """
        Create a Vector, example : v = Vector(1, 2)
        """
        if len(args) == 0:
            self.x, self.y = 0, 0
        else:
            self.x, self.y = args

    def __repr__(self):
        """
        Returns the Vector information
        """
        return "Vector(%r, %r)" % (self.x, self.y)

    def __add__(self, other):
        """
        Returns the Vector add
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)

    def __bool__(self):
        return bool(max(self.x, self.y))

# Vector 인스턴스 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

# 매직 메소드 출력
print("Ex3-1 - ", Vector.__init__.__doc__)
print("Ex3-2 - ", Vector.__repr__.__doc__)
print("Ex3-3 - ", Vector.__add__.__doc__)
print("Ex3-4 - ", v1, v2, v3)
print("Ex3-5 - ", v1+v2)
print("Ex3-6 - ", v1*4)
print("Ex3-7 - ", v2*10)
print("Ex3-8 - ", bool(v1), bool(v2))
print("Ex3-9 - ", bool(v3))
