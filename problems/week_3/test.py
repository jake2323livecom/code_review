keyboard = {
'2':'abc',
'3':'def',
'4':'ghi',
'5':'jkl',
'6':'mno',
'7':'pqrs',
'8':'tuv',
'9':'wxyz',
'0':' '
}

str_in = input()
def text(phrase):
    ls = []
    for char in phrase:
        for key,value in keyboard.items():
            for letter in value:
                if char == letter:
                    ls.append(key * int(value.index(letter) + 1))
    return(ls)

print(*text(str_in), sep = '-')