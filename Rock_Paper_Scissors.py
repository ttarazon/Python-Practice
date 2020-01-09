while True:
    win = 0
    game_on = input("Do you want to play ROCK PAPER SCISSORS, type yes or no ")
    if game_on == "no":
        break
    else:
        user_1 = input("Player 1 enter rock paper or scissors ")
        user_2 = input("Player 2 enter rock paper or scissors ")
    if user_1 == "rock" and user_2 == "scissors":
        print("Congratulations player 1, you won")
        win = 1

    if user_1 == "scissors" and user_2 == "paper":
        print("Congratulations player 1, you won")
        win = 1

    if user_1 == "paper" and user_2 == "rock":
        print("Congratulations player 1, you won")
        win = 1

    else:
        if win != 1:
            print("Congratulations player 2, you won")







