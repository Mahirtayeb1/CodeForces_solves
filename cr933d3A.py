# import random 
# code accepted in codeforces_round_933 d3 A
t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(m):
            if b[i]+c[j] <= k:
                count+=1
    print(count)


