
def Collatz(number):

        new_number = 0
        if number % 2 == 0:
            new_number = number // 2

        elif number % 2 == 1:
            new_number = 3 * number + 1
            

        return new_number

try:
 user_input = int(input(f"Please enter a number: "))
 print(Collatz(user_input))
except ValueError:
    print("Error: Not valid input. Please enter a number.\n")

