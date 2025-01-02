import random
import os
import subprocess

def bubble_sort(arr):
    """
    Sorts a list of numbers using the bubble sort algorithm.

    Args:
        arr: The list of numbers to be sorted.

    Returns:
        The sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    # Create a random list of numbers
    num_elements = 10  # Change this to adjust the list size
    random_list = [random.randint(1, 100) for _ in range(num_elements)]

    print("Unsorted List:", random_list)

    # Sort the list using bubble sort
    sorted_list = bubble_sort(random_list)

    print("Sorted List:", sorted_list)

    # Optional: Upload to GitHub (replace with your actual credentials)
    try:
        os.chdir("path/to/your/project/directory")  # Change to the project directory
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Commit message for sorting algorithm"])
        subprocess.run(["git", "push", "origin", "main"])  # Or your branch name
        print("Code uploaded to GitHub successfully!")
    except Exception as e:
        print(f"Error uploading to GitHub: {e}")