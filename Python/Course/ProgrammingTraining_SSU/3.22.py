n=1
sum = 0
while n <= 10000:
    match (n%2):
        case 1:
            sum += 4/(2*n-1)
            n += 1
        case 0:
            sum -= 4 / (2*n-1)
            n += 1

print(sum)

