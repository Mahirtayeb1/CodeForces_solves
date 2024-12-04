def numIdenticalPairs(nums):
        ans = 0    # list e i pointer protita indx thaika shob gula similer er count
        for i in range(len(nums)):
            count = 0   # runing i indx er shathe shob similer er count
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            ans += count
        return ans
        
num = [1,1,1,1]
ganja = [1,2,3]
print(numIdenticalPairs(num))
print(numIdenticalPairs(ganja))

# class Solution:
#     def numIdenticalPairs(self, nums):
#         ans = 0  # List e i pointer protita index theke shob gula similar er count
#         for i in range(len(nums)):
#             count = 0  # Running i index er shathe shob similar er count
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#             ans += count
#         return ans

# # Create an instance of the class
# solution = Solution()

# num = [1, 1, 1, 1]
# print(solution.numIdenticalPairs(num))
