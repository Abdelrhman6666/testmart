# Step 1: Take input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Step 2: Check for valid input (non-negative integer)
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Step 3: Initialize the result to 1 (factorial of 0 and 1)
    result = 1
    
    # Step 4: Loop to calculate the factorial
    for i in range(1, num + 1):
        result *= i  # Multiply result by each number from 1 to num
    
    # Step 5: Print the factorial
    print(f"The factorial of {num} is {result}")
