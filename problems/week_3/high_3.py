def main():
    # Test cases
    print(three_high([1, 2, 3, 4, 5]))
    print(three_high([12, 29, 48, 32, 1]))
    print(three_high([98, 38, 29, 3]))


def three_high(nums: list) -> list[int]:
    ''' Returns three highest numbers from provided list '''
    return sorted(nums)[-3:]


if __name__ == "__main__":
    main()