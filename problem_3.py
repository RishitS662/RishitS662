''' With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.'''

def generate_squared_dict(n):
    squared_dict = {}
    for i in range(1, n+1):
        squared_dict[i] = i*i
    return squared_dict

n = int(input("Enter a number: "))
result_dict = generate_squared_dict(n)
print(result_dict)
