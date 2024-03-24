start, end = 1.0, 2.0
repeat = 1

def mid(a, b):
    return (a+b)/2

def equation(a):
    val = a**2 - a - 1
    return val

while abs(equation(mid(start,end))) > 0.01 and repeat < 100 :

    if equation(mid(start, end)) > 0:
        end = mid(start,end)
    else:
        start = mid(start,end)

print(round(mid(start,end), 2))