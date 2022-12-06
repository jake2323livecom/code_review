def main():
    # Test cases
    print(sorting(['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'] , "length"))
    print(sorting(['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'] , "alphabetic"))
    
    # sorting(['thing'] , "failure") # Uncomment this line to test the ValueError


def sorting(tgt_list: list, sort_method: str) -> list:
    ''' Returns a list sorted based on given sort method
    - tgt_list: List to sort
    - sort_method: Type of sort to perform '''

    sort_types = [
        'length',
        'alphabetic'
    ]
    
    if sort_method not in sort_types:
        raise ValueError(f"The provided sort method is not an option")

    if sort_method == 'length': return sort_length(tgt_list)
    if sort_method == 'alphabetic': return sort_alpha(tgt_list)


# region Supporting functions
def sort_length(raw_list: list) -> list:
    ''' Returns a list sorted by word length '''
    
    raw_list.sort(key= lambda word: len(word))
    return raw_list


def sort_alpha(raw_list: list) -> list:
    ''' Returns a list sorted alphabetically '''
    
    raw_list.sort()
    return raw_list
    
# endregion


if __name__ == "__main__":
    main()