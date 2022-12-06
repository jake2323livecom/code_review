from math import ceil


def main():
    # Test cases
    print(find_avg([1,2,3,4,5]))
    print(find_avg([3,4,5,6]))
    print(find_avg([1,2,5,10]))


def find_avg(input_data:list) -> int:
    ''' Returns the average rounded up to the next integer'''
    
    return ceil(sum(input_data)/len(input_data))


if __name__ == "__main__":
    main()