''' Write a program that can compute the factorial of given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 5, 8, 3, 10. Then, the output should be: 120, 40320, 6, 3628800.'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numbers = [5, 8, 3, 10]

factorial_results = [str(factorial(num)) for num in numbers]
result = ', '.join(factorial_results)

print(result)
