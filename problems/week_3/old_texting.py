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
    print(f"'hello world' converts to: {texting('hello world')}")
    print(f"'idk my bff jill' converts to: {texting('idk my bff jill')}")
    print(f"'she mad woke frfr' converts to: {texting('she mad woke frfr')}")


def texting(message:str) -> str:
    ''' Returns a key code for testing on an old phone'''
    msg_len = len(message)
    key_code = ''.join([f"{KEYS[message[i]]}-" for i in range(msg_len)])
    
    return key_code[:-1]  # Removes the last '-' from the output


if __name__ == "__main__":
    main()