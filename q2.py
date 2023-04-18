def sum_recursion(n):
    """
    Calculates the sum of the equation ((-1)^(k+1))/k from k=1 to n using a recursive function and a global variable.

    :param n: The upper limit of the summation (inclusive)
    :type n: int
    """
    global result  # declare 'result' as a global variable

    if n == 0:
        result = 0
    else:
        sum_recursion(n - 1)
        result += ((-1) ** (n + 1)) / n

# Example usage
# the example usage of the function sets the global variable result to zero,
# calls sum_recursion with n=5, and then prints out the result of the summation.
result = 0
sum_recursion(5)
print(f"The sum of the equation is {result}")
