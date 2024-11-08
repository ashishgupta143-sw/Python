# Initialize variables
count = 0      # To keep track of how many odd numbers have been generated
number = 1     # The first odd number
sum_of_odds = 0  # To store the sum of the first 100 odd numbers

# Use a while loop to generate the first 100 odd numbers
while count < 100:
    print(number)             # Print the current odd number
    sum_of_odds += number     # Add the current odd number to the sum
    count += 1                # Increment the count of odd numbers
    number += 2               # Move to the next odd number

# Print the sum of the first 100 odd numbers
print("Sum of the first 100 odd numbers:",sum_of_odds)
