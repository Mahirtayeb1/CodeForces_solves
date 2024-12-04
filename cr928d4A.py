# a = 'ABAAB'
# count_a = 0
# count_b = 0 
# for i in range (len(a)):
#     if a[i] == "A":
#         count_a += 1
#     if a[i] == "B":
#         count_b += 1

# if count_a > count_b:
#     print('A')
# else:
#     print('B') 

t = int(input())
for i in range(t):
    a = input()  #.split()
    count_a = 0
    count_b = 0 
    for i in range (len(a)):
        if a[i] == "A":
            count_a += 1
        if a[i] == "B":
            count_b += 1

    if count_a > count_b:
        print('A')
    else:
        print('B') 

