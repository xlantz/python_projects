import random

def get_place_value_choice(number_name):
    places = {"1000th": 0.001, "100th": 0.01, "10th": 0.1, "1's": 1, "10's": 10, "100's": 100, "1000's": 1000}
    choice = input(f"Choose a place value for {number_name} {list(places.keys())}: ")
    return places.get(choice, 1)

def get_yes_no(prompt):
    return input(prompt).strip().lower() in ["yes", "y"]

def generate_number(place_value, allow_decimal, allow_exponent):
    base = random.uniform(1, 9) * place_value  # Ensures the number is within the correct range
    
    # Handle decimal inclusion
    if allow_decimal:
        if place_value >= 1:
            base += random.uniform(0, 0.99) * place_value  # Adds decimals relative to place value
        else:
            base = round(random.uniform(place_value, place_value * 9), 4)  # Ensures correct range
    
    # Handle exponentiation
    if allow_exponent:
        exponent = random.randint(1, 5)  # Exponent between 1 and 5
        base = round(base ** exponent, 4)  # Apply exponentiation and round
    
    return round(base, 4)

def main():
    while True:
        print("\n--- Number Generation Preferences ---")
        place_value1 = get_place_value_choice("first number")
        place_value2 = get_place_value_choice("second number")
        decimal_first = get_yes_no("Should the first number have decimals? (yes/no): ")
        decimal_second = get_yes_no("Should the second number have decimals? (yes/no): ")
        exponent_first = get_yes_no("Should the first number have an exponent? (yes/no): ")
        exponent_second = get_yes_no("Should the second number have an exponent? (yes/no): ")

        while True:
            num1 = generate_number(place_value1, decimal_first, exponent_first)
            num2 = generate_number(place_value2, decimal_second, exponent_second)
            while num1 == num2:  # Ensure numbers are different
                num2 = generate_number(place_value2, decimal_second, exponent_second)

            print(f"Generated Numbers: {num1}, {num2}")

            choice = input("\nWould you like to (1) Generate new numbers with the same preferences, (2) Change preferences, or (3) Quit? ")
            if choice == "2":
                break
            elif choice == "3":
                print("Goodbye!")
                return

if __name__ == "__main__":
    main()
