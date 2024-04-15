'''
import math
def pizza_area(radius: int) -> float:
    if radius > 0:
        area: float = math.pi * radius **2
        return area
    else:
        return 0

val, num = input('radius & number: ').split()
val = int(val)
num = int(num)

print(f'{val}cm 피자 {num}개의 면적은 {pizza_area(val)*num}입니다')

time_paid: int = int(input("time_paid: "))
time: int = int(input("time: "))
def money(time_paid: int, time: int) -> float:
    if time_paid >= 30:
        return time_paid*(30)+time_paid*1.5*(time-30)
    else:
        return time_paid*time
print (money(time_paid,time))

def addsub(x:int, y:int) -> tuple:
    return x-y, x+y
minus, add = addsub(10, 20)
'''