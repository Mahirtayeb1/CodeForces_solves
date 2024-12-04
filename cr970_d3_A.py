t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    g = a+(2*b)
    if (a % 2 == 0 and b == 0) or (a == 0 and b % 2 == 0):
        print("yes")
    elif (a % 2 != 0 and b == 0) or (a == 0 and b % 2 != 0):
        print("no")
    elif (b > a and b == g):
        print("yes")
    else:
        print("no")