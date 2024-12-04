def numdigit(n):
    digit = 0
    while(n!=0):
        n%10
        digit+=1
        n//=10
    return digit

print(numdigit(1000))

n = int(input())
f_twodig = int(str(n)[:2])
last_digits = int(str(n)[2:])
print(f_twodig)
print(last_digits)


# def numdigit(n):
#     digit = 0
#     while(n!=0):
#         n%10
#         digit+=1
#         n//=10
    
#     n // 10**digit
#     return n

# def first_twodigit(n):
#     n // 10**digit