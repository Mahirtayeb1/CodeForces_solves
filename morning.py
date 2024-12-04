def min_time_to_enter_pin(pin_code):
    current_position = 1  # Start with the cursor at digit '1'
    total_time = 0

    for digit in pin_code:
        if digit == '0':
            target_digit = 10  # Treat '0' as '10'
        else:
            target_digit = int(digit)
        
        # Calculate the time for both clockwise and counterclockwise movement
        clockwise_time = abs(target_digit - current_position)
        counterclockwise_time = 10 - clockwise_time
        # Choose the minimum time and add it to the total
        total_time += min(clockwise_time, counterclockwise_time)
        current_position = target_digit  # Move the cursor to the target digit

    # Add 4 seconds for pressing the button
    total_time += 4

    return total_time

# Test cases
test_cases = ["0000", "1111", "1211", "8269", "8361"]

for pin in test_cases:
    time = min_time_to_enter_pin(pin)
    print(f"{pin} = {time}")
