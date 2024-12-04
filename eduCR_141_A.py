for m in range(int(input())):
    n = int(input())
    x = []
    if n == 0:
        print('NO')
    if n == 1:
        print("NO")
    if n == 2:
        print('NO')
    else:
        for t in range(2, len(x)):
            for y in range(len(x)-1,0,-1):
