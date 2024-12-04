for m in range(int(input())):
    n = int(input())
    x = []
    if n == 3:
        print("NO")
        continue
    elif n%2 == 0:
        print("YES")
        for i in range(n//2):
            x.append("1")
            x.append("-1")
        print(" ".join(x))
        continue
    else:
        print("YES")
        y = n//2
        for j in range(n//2):
            x.append(str(1-y))
            x.append(str(y))
        x.append(str(1-y))
        print(" ".join(x))
        continue