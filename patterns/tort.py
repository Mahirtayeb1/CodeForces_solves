n = int(input())
arr = list(map(int, input().split()))
print(arr)
hare= 0
tortois = 0                      # 0 1 2
for i in range(2*n):            #  2 1 2 
    hare = arr[hare]          
    # if (hare == tortois):
    #     print(arr[hare])
    tortois = arr[tortois]
    tortois = arr[tortois]
    if (hare == tortois):
        print(arr[hare])

