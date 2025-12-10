num_guess = 0


print("Welcome to my guessing game!\n")
print("You have 3 guesses to guess the correct number from 1-10\n")

while num_guess < 4:
    user_guess = int(input("Guess: "))
    num_guess = num_guess + 1
    if user_guess == 7:
        print("Well done!")
        num_guess = 4
    else:
        continue


