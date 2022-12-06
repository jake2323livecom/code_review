# Find the 3 highest numbers (Difficulty 3 out of 10)
# Create a function to find the 3 largest numbers in a list.

# Your function should take a list of numbers as input and return the three highest numbers in descending order.

def request(numbers: list[int]) -> list[int]:
    '''
    Based on user input, determines and displays the three highest numbers in *descending* order.
    Extra info here...
    '''

    # Change the list from string to integers
    list_input = [int(digit) for digit in list_input]

    list_input.sort(reverse=True)

    return list_input[:3]

user_input = input("What are the numbers?: ")
'''Replace commas, if any, with spaces to facilitate the next part'''
remove_commas = user_input.replace(",", " ")
'''Split the input into a list, using spaces as the delineator'''
list_input = remove_commas.split()
print(request(list_input))