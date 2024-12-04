# A -> Primary Task

# t = int(input())
# for i in range(t):
#     n = int(input())
#     if(n<100):
#         print("No")
#     else:
#         f_twodig = int(str(n)[:2])
#         last_digs = int(str(n)[2:])
    
#         if (f_twodig == 10):
#             if (last_digs>2):
#                 print("Yes")
#             if(last_digs<=2):
#                 print("No")
#         else:
#             print("No")

"""previous one does not pass codeforces run time. 
So, this is the new one which will pass the runtime.  n = (1 -> 10000) """



t = int(input())
for i in range(t):
    n = int(input())
    if((n>=102 and n<=109) or (n>=1010 and n<=1099)):
        print("yes")
    else:
        print("no")

# 1100 1200 1999 2000 9999 10000