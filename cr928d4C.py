# def digit_sum(n):
    
#     return sum(int(digit) for digit in str(n))

# t = int(input())

# for i in range(t):
#     n = int(input())  
#     num_cycles = n // 9  
#     remainder = n % 9   
    
#     sum_1_to_9 = 45
    
#     total_sum = sum_1_to_9 * num_cycles + sum(i for i in range(1, remainder + 1))
    
#     print(total_sum)
def digit_sum(n):
    # Function to calculate the sum of digits of a number
    return sum(int(digit) for digit in str(n))

# Number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    n = int(input())  # Largest number Vladislav writes
    num_cycles = n // 9  # Calculate how many times numbers 1 to 9 appear
    remainder = n % 9   # Calculate the remainder
    
    # Calculate the sum of numbers 1 to 9
    sum_1_to_9 = 45
    
    # Calculate the sum of the numbers on the board
    total_sum = sum_1_to_9 * num_cycles + sum(i for i in range(1, remainder + 1))
    
    print(total_sum)
