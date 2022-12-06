# Old Fashioned Texting (Difficulty 6 out of 10)
# Remember trying to text on an older cell phone? You'd have to press a number multiple times to select a certain letter.

# Create a function to convert a string into number presses on an old cell phone. Separate each sequence by a hyphen.

'''Establish translation of letters to number presses'''
phone_translation = dict(a = "2", b = "22", c = "222", d = "3", e = "33", f = "333", g = "4", h = "44", i = "444", j = "5", k = "55", l = "555", m = "6", n = "66", o = "666", p = "7", q = "77", r = "777", s = "7777", t = "8", u = "88", v = "888", w = "9", x = "99", y = "999", z = "9999")

def create_sequence(list_input):
    sequence = ""
    index = 0
    for character in list_input:
        if character == " ":
            sequence += "0"
        else:
            sequence += phone_translation.get(character)
        index += 1
        '''Adds a hyphen between each iteration; stops adding hyphen if at the end of the list'''
        if index < len(list_input):
            sequence += "-"
    return sequence

user_input = input("What's the sentence?: ")
list_input = [*user_input]
print(create_sequence(list_input))