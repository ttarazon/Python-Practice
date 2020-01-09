number_var = int(input("Please enter a number "))
list_var = list(range(1, number_var+1))
list_output = []
for number in list_var:
    if number_var % number == 0:
        list_output.append(number)

print(list_output)


