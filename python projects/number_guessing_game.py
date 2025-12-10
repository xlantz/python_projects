import random

user_number = 0

number_of_guesses = 0

random_number = random.randint(1,20)

while user_number != random_number:
    user_number = int(input("Please guess a number: "))

    number_of_guesses = number_of_guesses + 1
    
    if user_number < random_number:
        print("\nNumber too low.\n")
    elif user_number > random_number:
        print("\nNumber too high.")
    else:
        print(f"\nGood job. You guessed the number in {number_of_guesses} tries.")