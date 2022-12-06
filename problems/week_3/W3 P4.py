# Old Fashioned Texting (Difficulty 6 out of 10)
# Remember trying to text on an older cell phone? You'd have to press a number multiple times to select a certain letter.

# Create a function to convert a string into number presses on an old cell phone. Separate each sequence by a hyphen.

'''Establish translation of letters to number presses'''
PHONE_TRANSLATION = dict(
    a = "2", 
    b = "22", 
    c = "222",
    d = "3", 
    e = "33", 
    f = "333", 
    g = "4", 
    h = "44", 
    i = "444", 
    j = "5", 
    k = "55", 
    l = "555", 
    m = "6", 
    n = "66", 
    o = "666", 
    p = "7", 
    q = "77", 
    r = "777", 
    s = "7777", 
    t = "8", 
    u = "88", 
    v = "888", 
    w = "9", 
    x = "99", 
    y = "999", 
    z = "9999")


def texting_sequence(list_input: list) -> str:
    '''Translates a user-inputted word into the number sequences required to text on phones with a physical keypad'''
    sequence = ""
    for index, character in enumerate(list_input):
        if character == " ":
            sequence += "0"
        else:
            sequence += phone_translation.get(character)
        '''Adds a hyphen between each iteration; stops adding hyphen if at the end of the list'''
        if index  < len(list_input) - 1:
            sequence += "-"
    return sequence

def texting_sequence(characters: list[str]) -> str:
    '''Translates a user-inputted word into the number sequences required to text on phones with a physical keypad'''

    PHONE_TRANSLATION = dict(
        a = "2", 
        b = "22", 
        c = "222",
        d = "3", 
        e = "33", 
        f = "333", 
        g = "4", 
        h = "44", 
        i = "444", 
        j = "5", 
        k = "55", 
        l = "555", 
        m = "6", 
        n = "66", 
        o = "666", 
        p = "7", 
        q = "77", 
        r = "777", 
        s = "7777", 
        t = "8", 
        u = "88", 
        v = "888", 
        w = "9", 
        x = "99", 
        y = "999", 
        z = "9999"
    )

    sequences = []
    for character in characters:
        if character == " ":
            pattern = "0"
        else:
            pattern = PHONE_TRANSLATION.get(character)

        sequences.append(pattern)

    return '-'.join(sequences)

'''Takes the user input and lazily makes it all lower case; otherwise it would error out'''
user_input = input("What's the sentence?: ").lower()
list_input = list(user_input)
print(texting_sequence(list_input))