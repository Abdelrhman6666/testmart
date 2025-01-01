# Step 1: Take input from the user
num = int(input("Enter a number to find prime numbers up to that limit: "))

# Step 2: Start the loop and apply the algorithm
print(f"Prime numbers up to {num} are:")
for number in range(2, num + 1):  # Check numbers from 2 to num
    # Assume the number is prime
    is_prime = True
    
    # Check if the number is divisible by any number smaller than it
    for i in range(2, number):
        if number % i == 0:
            is_prime = False  # Not prime if divisible by any number other than 1 and itself
            break  # No need to check further
    
    # Step 3: Print the prime numbers inside the loop
    if is_prime:
        print(number)
