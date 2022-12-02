def find_average(input):
    quan = 0
    total = 0
    for i in input:
        quan += 1
        total += int(i)
    average = total / quan
    return int(average)

orig_input = input("What are the numbers? ")
remove_spaces = orig_input.replace(" ", "")
list_input = list(remove_spaces.replace(",", ""))
print(find_average(list_input))