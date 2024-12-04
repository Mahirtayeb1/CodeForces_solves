# t = int(input())
# for i in range(t):
    
# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    # for j in range(0, len(array) - i - 1):
    for j in range(i+1, len(array)):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[i] > array[j]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        



data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Descending Order:')
print(data)