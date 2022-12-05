#     ##########################
#     ### Find An Easter Egg ###
#     ##########################


# import this


#     ##################################
#     ### Find The 3 Highest Numbers ###
#     ##################################


# def numbers(list):
    
#     highest_3 = list
#     highest_3.sort()
#     highest_3.reverse()
#     print(highest_3[0:3])
    
# numbers([100, 4, 888, 432, 999])


#     ###################################
#     ### Add a Number To Its Reverse ###
#     ###################################


# def reverse_number():
    
#     num = int(input("Please Enter A Number: "))
#     new_num = int((str(num)[::-1]))
#     final_num = num + new_num
#     return final_num
    
    
# print(reverse_number())


#     #############################
#     ### Old Fashioned Texting ###
#     #############################
   
   
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

old_fashion_text("she mad woke frfr")