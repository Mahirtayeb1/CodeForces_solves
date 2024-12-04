t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    brdg = (n*(n-1))/2
    if k == 0 or k > n/2:
        print(n)
    if k >= n or k >= brdg:
        print(1)
    else:
        print(n)
    
        

