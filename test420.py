def find():
    n = int(input('number'))
    a = 0
    for i in range(n+1):  # suming prev num+current num 
        a = a+i
        print(a)
find()



#x = [i for i in range(10) if i%2 == 0]
#print(x)

n = int(input("num: "))
a = 0
for i in range(n+1):
    a = a + i
    print(a)

n = int(input("num: "))
for i in range(1, n+1):   # suming all numbers till n
    print(i)


n = input()
x = n.upper()
print(x)

