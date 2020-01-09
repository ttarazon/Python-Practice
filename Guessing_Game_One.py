import random
random_var = random.randint(1, 9)


def user_input_function():
    count = 0
    game_on = "yes"
    while game_on != "no":
        user_num = input("Please enter a number between 1 and 9 ")
        count += 1
        if int(user_num) > random_var:
            print("Your number is higher than the randomly chosen number")
        if int(user_num) < random_var:
            print("Your number is lower than the randomly chosen number")
        if int(user_num) == random_var:
            print("You guessed the randomly chosen number in %d attempts" % count)
            break
        game_on = input("Do you want to continue, yes or no ")

user_input_function()
print("The randomly chosen number is %d " % random_var)
