from itertools import islice
t = int(input())
for p in range(t):
    n = int(input())
    arr = list(islice(map(int, input().split()), n))
    butyful_segment = 0
    for i in arr:
        if arr[i] == 0:
            butyful_segment+=1
    print(butyful_segment)   

