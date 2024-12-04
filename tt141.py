x = [1,2,3,6]
print(len(x)) 
print(x[len(x)-1]) # printing last element 
t = []
for i in range(len(x)-1,0,-1):  # strt, stop, step
    t.append(x[i])
print(t)

#q = int(input())
arr = [0] * int(input())
print(len(arr))
print(arr)