    ##########################
    ### Find An Easter Egg ###
    ##########################


print('#' * 30 + " PART I " + '#' * 30)

import this
print()


    ##################################
    ### Find The 3 Highest Numbers ###
    ##################################


print('#' * 30 + " PART II " + '#' * 30)

def numbers(list):

    highest_3 = list
    highest_3.sort()
    highest_3.reverse()
    print(highest_3[0:3])
    print()

numbers([100, 4, 888, 432, 999])


    ###################################
    ### Add a Number To Its Reverse ###
    ###################################


print('#' * 30 + " PART III " + '#' * 30)

def reverse_number():

    num = int(input("Please Enter A Number: "))
    print(f"Your number is: {num}")
    new_num = int((str(num)[::-1]))
    print(f"Your number in reverse is: {new_num}")
    final_num = num + new_num
    print(f"Your number plus your number in reverse is: {final_num}")
    print()

reverse_number()


    #############################
    ### Old Fashioned Texting ###
    #############################


print('#' * 30 + " PART IV " + '#' * 30)

def old_fashion_text (string) :

    keypad = {
    '1' : ['.', ',', '?', '!', ':'],
    '2' : ['A', 'B', 'C'],
    '3' : ['D', 'E', 'F'],
    '4' : ['G', 'H', 'I'],
    '5' : ['J', 'K', 'L'],
    '6' : ['M', 'N', 'O'],
    '7' : ['P', 'Q', 'R', 'S'],
    '8' : ['T', 'U', 'V'],
    '9' : ['W', 'X', 'Y', 'Z'],
    '0' : [' ']
    }

    txt = string.upper()

    result = ""
    keys = list(keypad.items())

    for i in range(len(txt)):
        for j in range(len(keys)):
            for k in range(len(keys[j][1])):
                if txt[i] == keys[j][1][k]:
                    result+=((k+1)*keys[j][0])
                    result += '-'

    print(result)
    print()

old_fashion_text("she mad woke frfr")


    #######################
    ### Friday the 13th ###
    #######################
    
    
print('#' * 30 + " PART IV " + '#' * 30)

# def friday_the_13th(range()):
#     pass

# friday_the_13th(2010, 2022)