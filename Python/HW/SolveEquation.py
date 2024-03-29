#시작구간, 끝구간
start, end = 1.0, 2.0
repeat: int = 1

#탐색구간의 중간값을 리턴
def mid(a, b):
    return (a+b)/2

#주어진 식에 값을 입력한 값을 리턴
def equation(a):
    val = a**2 - a - 1
    return val

#함수 호출을 줄이기 위해서 중간 변수 설정
val = mid(start, end)

#함수값이 오차범위보다 크거나 반복횟수가 100회 미만일때 while 루프
while abs(equation(val)) > 0.01 and repeat < 100 :

    if equation(val) > 0: 
        end = val
        val = mid(start,end) #중간값 갱신
    else:
        start = val
        val = mid(start, end) #중간값 갱신

print(round(val, 2))