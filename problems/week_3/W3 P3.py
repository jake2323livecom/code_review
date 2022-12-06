# Add a number to its reverse (Difficulty 4 out of 10)

# Create a function to reverse the digits of a given number and add it to the original.

def thing(list_input: list) -> int:
    '''Determines the reverse digits of a user-inputted number, and adds the two numbers together'''
    second_number = ""
    '''Iterates the list backwards to establish the reversed number'''
    for digit in list_input[-1::-1]:
        second_number += digit
    '''Adds the original number to the newly determined second number'''
    return int(user_input) + int(second_number)    

user_input = input("What is the number?: ")
'''Unpacks the string into a list. Can't use .split() since there's no delineators'''
list_input = [*user_input]
print(thing(list_input))