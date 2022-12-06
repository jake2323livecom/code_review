import calendar
from datetime import date


def main():
    # Test cases
    print(fri_find('2019'))
    print(fri_find('1995'))
    print(fri_find('1980'))


def fri_find(year:str) -> list[str]:
    ''' Returns the months that have a Friday the 13th for a given year'''

    # Create integer-based list of months with friday the 13th
    months = []
    for month in range(1,13):
        if date(int(year), month, 13).weekday() == 4:
            months.append(month)

    ##### Optional solution for above code with a list comprehension #####
    # months = [month for month in range(1,13) if date(int(year), month, 13).weekday() == 4]

    # Return a human readable list of months with friday the 13th
    return [calendar.month_name[month_num] for month_num in months]


if __name__ == "__main__":
    main()