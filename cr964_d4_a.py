n = int(input())
for i in range(n):
    m = int(input())
    g = 0
    while(m!=0):
        g += m%10
        #print(m%10)
        m//=10
    print(g)

# m = int(input())
# while(m!=0):
#     print(m%10)
#     m//=10