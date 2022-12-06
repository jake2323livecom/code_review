def main():
    # Test cases
    print(adds_zeros("some_string", 3))
    print(adds_zeros("some_string", 1))
    print(adds_zeros("some_string", 5))


def adds_zeros(string_input:str, zero_count:int) -> str:
    ''' Returns a string with the addition of leading zeros
    - string_input: Base string
    - zero_count: Number of zeros to add to the base string'''
    
    return f"{'0'*zero_count}{string_input}"


if __name__ == "__main__":
    main()