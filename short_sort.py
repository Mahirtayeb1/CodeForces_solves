x = int(input())
for i in range(x):
    str = input()
    if str == "abc":
        print("yes")
    elif str[0] == 'a':
        print("yes")
    elif str[0] == 'b' and str[1] == 'a':
        print('yes')
    elif str[2] == 'a' and str[0] == 'c':
        print('yes')
    elif str[1] == 'a' and str[0] == 'c':
        print('no')
    else:
        print("no")