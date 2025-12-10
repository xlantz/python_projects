from datetime import datetime
current_datetime = datetime.now()
current_year = current_datetime.year

name = input("What's your name?")
print(f"Hello, {name.capitalize()}")
print("Let's get to know each other.")
favorite_color = input("What's your favorite color? ")
age = input("What's your age? ")
place_from = input("Where are you from? ")

print(f"Hello {name}, age {age}.\n Your favorite color is {favorite_color},\n and you're from {place_from}.\n")

birth_year = current_year - int(age)

print(f"The year you were born was {birth_year}\n")

