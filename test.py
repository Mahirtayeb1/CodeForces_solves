# n = int(input())
# for i in range(len(n)):
#     a = []*int(input())
#     sum_a = sum(a)
#     for i in range(len(a)):
#       for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#           print("No")
#         if sum_a - a[i] == a[j]:
#           print("Yes")
#     print("No")

# arr = []*int(input())
# for j in range(len(arr)):
#   if len(arr) == 2 and arr[0] == arr[1]:
#     print("Yes")
#   if len(arr) == 2 and arr[0] != arr[1]:
#     print("No")

# array = [1, 2, 4, 3, 2, 3, 5, 4]
# array = [2,3]
array = list(map(int, input().strip().split()))

sum_of_odds = 0
sum_of_evens = 0
for element in array:
  if element % 2 == 1:
    sum_of_odds += element
  else:
    sum_of_evens += element

if sum_of_odds == 0 or sum_of_evens == 0:
  print("Yes")
elif ((sum_of_odds + 1) % 2 == (sum_of_evens - 1) % 2)):
  print("No")

