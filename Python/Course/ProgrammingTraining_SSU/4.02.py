'''
class Coll:
    def __init__(self,d):
        self.ds = d

    def __iter__(self):
        print('iter 호출')
        return self

c = Coll([1,2,3,4])
for i in c:
    print(i)


class Coll:
    def __init__(self,d): #스페셜 메소드는 클래스에 기본적으로 존재하는 매소드를 오버라이딩함
        self.ds = d

    def __next__(self):  # iter함수의 iterator 반환값을 next method의 argument로 받는 것에 def로 오버라이딩
        print('next 호출') # __iter__의 self 반환값을 __next__의 argument로 입력
        if len(self.ds) <= self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc - 1]

    def __iter__(self):
        print('iter 호출')
        self.cc = 0
        print(type(self))
        return self

c = Coll([1,2,3,4])
for i in c:  # for문의 작동방식 iter(c)-->c.__iter__()--> iterator 객체를 반환 --> __next__(iterator 객체)
    print(i) #하지만 special method의 next, init method를 통해 변형시킴


class IterMethod:
    def __init__(self):
        pass

    def __iter__(self):
        i = 5
        while i <= 50:
            print(f"this is {i}")
            i = i + 10
        return self


my_iter = IterMethod()


import random
distance = round(random.uniform(1,2),1)
init_price = 4800
if distance <= 1.6:
    total_price = 4800
else:
    total_price = int(4800 + (distance - 1.6))
print(f'{distance} costs {total_price}')
'''

# Import Self
from typing import Self

# Define a base class
class Car:
	def set_brand(self,
				brand: str) -> Self:
		self.brand = brand
		return self

# Define a child class
class Brand(Car):
	def set_speed(self,
				speed: float) -> Self:
		self.speed = speed
		return self

# Calling object inside print statement
print(Car().set_brand("Maruti"))
print(Brand().set_brand("Maruti").set_speed(110.5))
print(type(Car().set_brand("Maruti")))
print(type(Brand().set_brand("Maruti").set_speed(110.5)))
