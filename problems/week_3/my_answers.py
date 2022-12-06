import this

def high_three(nums: list) -> list:
    """Returns the highest three numbers in a list in descending order."""

    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[:3]

print(high_three([1, 2, 3, 4, 5]))
print(high_three([12, 29, 48, 32, 1]))
print(high_three([98, 38, 29, 3]))

def rev_number(num: int) -> int:
    """Adds a number to the reversed version of itself."""

    reversed_number = str(num)[::-1]

    return num + int(reversed_number)


print(rev_number(21))
print(rev_number(32))
print(rev_number(123))
print(rev_number(3548))

def texting(string: str) -> str:
    """
    Shows the old texting pattern for a message.

    Takes a message containing any alphabetic characters and translate it into a number of key press patterns. 
    Future version will support numbers as well.
    
    Parameters:
        string (str): Any user inputted string.  Can contain only letters.

    Returns:
        str: Returns a series of number presses on an old cell phone.
    """

    keypad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '
    }

    
    patterns = []

    for char in string:
        if char.isalpha() or char.isspace():
            for num, letters in keypad.items():
                if char in letters:
                    pattern = num * (letters.index(char) + 1)
                    patterns.append(pattern)
        else:
            raise ValueError('The inputted string must contain only letters and spaces.')


    return '-'.join(patterns)

print(texting('hello world'))
print(texting('idk my bff jill'))
print(texting('she mad woke frfr'))

