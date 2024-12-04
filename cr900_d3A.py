x = int(input())
for i in range(x):
    m, t = map(int, input().split()) # m = arr size & t = max
    arr = list(map(int, input().strip().split()))
    mx = 0 # counting max
    cc = 0 # current count
    for i in range(m):
        if arr[i] == t:
            cc += 1
        else:
            cc = 0
        
        max_count = max(mx, cc)
    if mx > 0:
        print("yes")
    else:
        print("no")