# region Static vars
KEYS = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    ' ': '0'
}
# endregion


def main():
    #Test cases
    print(texting('hello world'))
    print(texting('idk my bff jill'))
    print(texting('she mad woke frfr'))


def texting(message:str) -> str:
    ''' Returns a key code for testing on an old phone'''

    # Creates the list of keys to push
    keys_to_push = [f"{KEYS[message[i]]}" for i in range(len(message))]
    
    # Adds a '-' between each key code
    return '-'.join(keys_to_push)
    

if __name__ == "__main__":
    main()