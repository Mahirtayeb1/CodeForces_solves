n = int(input())  # Number of test cases

for _ in range(n):
    # Read the number of digits and the list of digits for each test case
    num_digits = int(input())  # Number of digits
    digits = list(map(int, input().strip().split()))  # List of digits
    
    # Find the smallest digit in the array
    min_digit = min(digits)
    
    # Find the index of the first occurrence of the smallest digit
    min_digit_index = digits.index(min_digit)
    
    # Add 1 to the smallest digit
    digits[min_digit_index] += 1
    
    # Calculate the product of all digits
    product = 1
    for digit in digits:
        product *= digit
    
    # Print the maximum product
    print(product)
