import math 
t = int(input())
for i in range(t):
    x, y = map(int, input().split()) 
    calcY = math.ceil(y/2)
    calcX = math.ceil(x/15)
    if y == 0:
        print(calcX)
    elif y % 2 == 0:
        if x <= 7:
            print(calcY + int(math.floor(x/15)))
        else:
            print(int(calcY) + int(calcX))
    elif y % 2 == 1:
        if x <= 11:
            print(calcY)
        else:
            print(int(calcY) + int(calcX))
