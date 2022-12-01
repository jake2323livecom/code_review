    ##########################
    ### Find An Easter Egg ###
    ##########################


import this


    ##################################
    ### Find The 3 Highest Numbers ###
    ##################################


def numbers(list):
    
    highest_3 = list
    highest_3.sort()
    highest_3.reverse()
    print(highest_3[0:3])
    
numbers([100, 4, 888, 432, 999])


    ###################################
    ### Add a Number To Its Reverse ###
    ###################################


def reverse_number():
    
    num = int(input("Please Enter A Number: "))
    new_num = int((str(num)[::-1]))
    final_num = num + new_num
    return final_num
    
    
print(reverse_number())


    #############################
    ### Old Fashioned Texting ###
    #############################
    

