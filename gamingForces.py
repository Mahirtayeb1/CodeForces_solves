t = int(input())
for i in range(t):
    n = int(input())
    var = input().split()
 
    myList = []
    for j in var:
        myList.append(int(j))
    myList.sort()
 
    counter = 0
    while len(myList) > 0:
        if len(myList) > 1:
            if myList[0] == myList[1] and myList[0] <= 2:
                counter += myList[0]
                myList.pop(0)
                myList.pop(0)
            else:
                counter += 1
                myList.pop(0)
        else:
            counter += 1
            myList.pop(0)
    print(counter)