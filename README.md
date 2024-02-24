'''Reverse the contents of the file1.txt.'''

# Read the contents of the file
with open('f1.txt', 'r') as file:
    lines = file.readlines()

# Reverse the lines
reversed_lines = reversed(lines)

# Write the reversed lines back to the file
with open('f1.txt', 'w') as file:
    file.writelines(reversed_lines)
