def create_list(user_input):
    counter = 0
    list_output = []
    while counter != user_input:
        counter += 1
        list_output.append(2**counter)
        print(counter)
    return list_output

user_input = int(input("What is the number? "))
print(create_list(user_input))