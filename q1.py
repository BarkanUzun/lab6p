from math import factorial

# Take user input for n and x
n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))

# Define the lambda function for the equation
f = lambda n, x: sum([(n**i) / factorial(i) for i in range(x+1)])

# Call the lambda function with user input values
result = f(n, x)

# Print the result
print(f"The result of the equation is {result}")
