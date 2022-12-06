# Find the 3 highest numbers (Difficulty 3 out of 10)
# Create a function to find the 3 largest numbers in a list.

# Your function should take a list of numbers as input and return the three highest numbers in descending order.

def request():
    list_output = []
    '''Change the list from string to integers'''
    for digit in list_input:
        list_output.append(int(digit))
    '''Sort the list in *descending* order'''
    list_output.sort(reverse=True)
    '''Return the first three list items'''
    return list_output[0:3]

user_input = input("What are the numbers?: ")
'''Replace commas, if any, with spaces to facilitate the next part'''
remove_commas = user_input.replace(",", " ")
'''Split the input into a list, using spaces as the delineator'''
list_input = remove_commas.split()
print(request())