def main():
    #Test cases
    print(add_reverse(21))
    print(add_reverse(32))
    print(add_reverse(123))
    print(add_reverse(3548))


def add_reverse(num:int) -> int:
    ''' Returns the sum of a number and its reverse '''
    return num + int(str(num)[::-1])


if __name__ == "__main__":
    main()