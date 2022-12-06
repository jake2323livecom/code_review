def main():
    # Test cases
    print(get_powers_of_2(5))
    print(get_powers_of_2(12))
    print(get_powers_of_2(13))


def get_powers_of_2(number:int) -> list:
    ''' Returns a list of the powers of 2 for a given number'''
    
    return [2**i for i in range(1, number + 1)]


if __name__ == "__main__":
    main()