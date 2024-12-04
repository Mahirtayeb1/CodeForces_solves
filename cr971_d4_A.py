t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = (a+b)//2
    minres = (c-a)+(b-c)
    print(minres)
