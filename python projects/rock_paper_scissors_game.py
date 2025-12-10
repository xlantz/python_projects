import random

my_list = ["rock", "paper", "scissors"]

user_move = None

user_win = 0

user_lose = 0

user_tie = 0

while user_move != "q":

    comp_move = random.choice(my_list)

    print(f"Wins: {user_win} Losses: {user_lose} Ties: {user_tie}\n")

    user_move = input("Please enter a move [(r)ock, (p)aper, (s)cissors, or (q)uit]: ")

    if user_move == "r":
        if comp_move == "rock":
            print("It's a tie.")
            user_tie += 1
        elif comp_move == "scissors":
            print("You win.")
            user_win += 1
        elif comp_move == "paper":
            print("You lose.")
            user_lose += 1

    elif user_move == "p":
        if comp_move == "paper":
            print("It's a tie.")
            user_tie += 1
        elif comp_move == "rock":
            print("You win.")
            user_win += 1
        elif comp_move == "scissors":
            print("You lose.")
            user_lose += 1

    elif user_move == "s":
        if comp_move == "scissors":
            print("It's a tie.")
            user_tie += 1
        elif comp_move == "paper":
            print("You win.")
            user_win += 1
        elif comp_move == "rock":
            print("You lose.")
            user_lose += 1
    
    elif user_move == "q":
        print("Sorry to see you go.")

    else:
        print("Invalid move.")