n = int(input())
for i in range(n):
    arr = list(map(int, input().strip().split()))
    sum_of_odds = 0
    sum_of_evens = 0
    for element in array:
        if element % 2 == 1:
            sum_of_odds += element
        else:
            sum_of_evens += element

    if sum_of_odds == 0 or sum_of_evens == 0:
        print("Yes")
    elif ((sum_of_odds + 1) % 2 == (sum_of_evens - 1) % 2)):
        print("No")


