n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    #print(a,b,c)
    #pd = a*b*c
    count = 0
    while(count < 5):
    #for count in range(5):
        if(a<=b and a<=c):
            a+=1
            print(a)
            count+=1
            print("g",count)
        elif(b<=a and b<=c):
            b+=1
            print(b)
            count+=1
            print("g",count)
        elif(c<=a and c<=b):
            c+=1
            print(c)
            count+=1
            print("g",count)
    print(a*b*c)