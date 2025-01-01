# Fibonacci Sequence Generator

# Step 1: Define the required variables
n = int(input("Enter the number of Fibonacci numbers you want: "))  # User input

# Step 2: Initialize the first two Fibonacci numbers
a, b = 0, 1

# Step 3: Loop to get the Fibonacci numbers
for i in range(n):
    print(a)  # Print the current Fibonacci number
    a, b = b, a + b  # Update a and b to the next Fibonacci numbers
