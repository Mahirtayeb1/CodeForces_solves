x = int(input())
for i in range(x):
    arr = list(map(int, input().strip().split()))

    for digit in arr:
        if digit == '0':
            tar_digt = 10
        else:
            tar_digt = int(digit)
    
    time = abs(1-pin[i])+abs(pin[i-1] - pin[i])+abs(pin[i-1] - pin[i])+abs(pin[i-1] - pin[i]) + 4