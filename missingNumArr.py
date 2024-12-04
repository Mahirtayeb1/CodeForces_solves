def missingNumArr(num):
    n = len(num)
    expected = n * (n + 1) // 2
    total = sum(num)
    missing = expected - total
    return missing

l = [2,3,0,1]
print(missingNumArr(l))

