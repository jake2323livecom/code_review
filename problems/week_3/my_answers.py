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
    """Shows the old texting pattern for a message."""

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
        for num, letters in keypad.items():
            if char in letters:
                pattern = num * (letters.index(char) + 1)
                patterns.append(pattern)

    return '-'.join(patterns)

print(texting('hello world'))
print(texting('idk my bff jill'))
print(texting('she mad woke frfr'))

from calendar import Calendar

def fridays(year: int) -> list:
    """Returns every month in a year that has a friday the 13th."""

    # Create a list of month names.  This will come in handy later.
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    # Create a generic Calendar object instance
    all_time = Calendar()

    
    # Use a class method to grab all the days of a particular year.  
    # For some reason this method returns a list where the entire year's months are kept in the first item, 
    # so we go ahead and set the year variable to the first index of the result of the function call.
    year = all_time.yeardays2calendar(year=year, width=12)[0]

    # Create empty result list
    result = []

    # Loop through each month in the year.  We use enumerate so that we will have the month's index number.  
    # This is what we will use to pull the month's name from the above list.
    for index, month in enumerate(year):
        for week in month:
            for day in week:

                # The day is a tuple containing the day number (out of the month) and weekday number, so we unpack it into two variables.
                day_number, weekday_number = day

                # If the day number is 13 and the weekday number is 4 (friday), then we use the index to pull the correct month name from the months list.
                if day_number == 13 and weekday_number == 4:
                    result.append(months[index])

    return result

print(fridays(2019))
print(fridays(1995))
print(fridays(1980))
