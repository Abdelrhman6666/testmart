def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n: The non-negative integer.

    Returns:
        The factorial of n.
    """
    if n == 0:  # Base condition: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive return

if __name__ == "__main__":
    number = 5
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")