"""
Prompting the user for two numbers and summing them and when the input 
isn't a number we catch an exception and the program continues to run.
"""

try:
    number0 = int(input('Enter the first number: '))
    number0 += int(input('Enter the second number: '))
    print(number0)
except ValueError:
    print('Please enter only integers!')

