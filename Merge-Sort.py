import random

# Step 1: Create a random list of numbers
arr = [random.randint(1, 100) for _ in range(10)]  # List of 10 random numbers between 1 and 100
print("Original List:", arr)

# Step 2: Bubble Sort Algorithm
n = len(arr)

# Outer loop for multiple passes
for i in range(n):
    swapped = False  # Flag to check if any swap was made in the current pass
    
    # Inner loop for comparing adjacent elements
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # Swap elements if they are in the wrong order
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True  # Mark that a swap occurred
    
    # If no swaps were made, the list is already sorted
    if not swapped:
        break

# Step 3: Print the sorted list
print("Sorted List:", arr)
