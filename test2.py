# x = 7
# print(x / 15)
def dupli(nums):
    for i in range(len(nums)-1):
        #j = i + 1
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
            
    return False

a = [1, 2, 3, 4]
print(dupli(a))

b = [1, 2, 3, 3]
print(dupli(b))

# def multiply_multinum(*args):
#     return sum(args)
    
# result = multiply_multinum(1,2,3,4,5,6,2,4,56,2,4,5,2)
# print(multiply_multinum(result))