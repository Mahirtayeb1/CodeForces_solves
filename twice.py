from itertools import islice
t = int(input())
for p in range(t):
    n = int(input())
    arr = list(islice(map(int, input().split()), n))
    newarr = []
    k_score = 0
    for i in range(n):
        if arr[i] not in newarr:
            newarr.append(arr[i])
            ele = 1
            for j in range(i+1, n):
                #ele = 1
                if arr[i] == arr[j]:
                    ele+=1
                #print(ele)
            k_score += ele//2
            #print(k_score)
            #ele = 1
        else:
            continue

    print(int(k_score)) 

#print(3//2)