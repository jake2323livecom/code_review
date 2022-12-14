def add_zeroes(zeroes, string_input):
    zero_string = ""
    while zeroes != 0:
        zero_string += str(0)
        zeroes -= 1
        #print(zeroes)
    return zero_string + string_input

zero_input = int(input("How many zeroes? "))
string_input = input("What's the string? ")
print(add_zeroes(zero_input, string_input))