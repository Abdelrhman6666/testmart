import random

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
    # Generate a random list of numbers
    num_elements = 10  # Change this to adjust the list size
    random_list = [random.randint(1, 100) for _ in range(num_elements)]

    print("Unsorted List:", random_list)

    # Sort the list using bubble sort
    sorted_list = bubble_sort(random_list)

    print("Sorted List:", sorted_list)