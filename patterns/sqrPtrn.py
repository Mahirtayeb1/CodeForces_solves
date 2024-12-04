# n = int(input())
# for row in range(n):
#     for colmn in range(n):
#         print("*", end = "")
#     print("")

n = int(input())
for row in range(1,n+1):
    for colmn in range(n-row):
        print(" ", end = "")
    for colm in range(row):
        print("*", end="")
    # for colmn in range(n-row):
    #     print(" ", end = "")
    print("")


