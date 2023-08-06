import random


def pr_red(skk): print("\033[91m {}\033[00m".format(skk))


def pr_green(skk): print("\033[92m {}\033[00m".format(skk))


def pr_yellow(skk): print("\033[93m {}\033[00m".format(skk))


rock = "Rock"
paper = "Paper"
scissors = "Scissors"
win_counter = 0
lose_counter = 0
draw_counter = 0
game_session = 0
player_move = input("Choose [r]ock, [p]aper ot [s]issors: ")
game_is_on = True
while game_is_on:
    if player_move == "r":
        player_move = rock
        print("You chose Rock.")
    elif player_move == "p":
        player_move = paper
        print("You chose Paper.")
    elif player_move == "s":
        player_move = scissors
        print("You chose Scissors.")
    else:
        print("Invalid input. Try again!")
        player_move = input("Choose [r]ock, [p]aper ot [s]issors: ")

    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        pr_green("You win!")
        win_counter += 1
    elif player_move == computer_move:
        pr_yellow("Draw!")
        draw_counter += 1
    else:
        pr_red("You lose!")
        lose_counter += 1
    game_session += 1

    question_new_game = input("Would you like to play again? Choose Yes (press y) or No (press n): ")
    if question_new_game == "y":
        player_move = input("Choose [r]ock, [p]aper ot [s]issors: ")
    elif question_new_game == "n":
        question_score = input("Would you like to see your score? Choose Yes (press y) or No (press n): ")
        if question_score == "y":
            print(f"Games played: {game_session} \nWin: {win_counter} \nLoss: {lose_counter} \nDraw: {draw_counter}")
            print("Thank you for playing Rock-Paper-Scissors!")
            game_is_on = False
            exit()
        elif question_new_game == "n":
            print("Thank you for playing Rock-Paper-Scissors!")
            game_is_on = False
            exit()
        else:
            print("Invalid input. Try again!")
            player_move = input("Choose [r]ock, [p]aper ot [s]issors: ")
    else:
        print("Invalid input. Try again!")
        question_new_game = input("Would you like to play again? Choose Yes (press y) or No (press n): ")

    # question_score = input("Would you like to see your score? Choose Yes (press y) or No (press n): ")
    # if question_score == "y":
    #     print(f"Games played: {game_session} Win: {win_counter} Loss: {lose_counter} Draw: {draw_counter}")
    # elif question_new_game == "n":
    #     continue
    # else:
    #     raise SystemExit("Invalid input. Try again!")
