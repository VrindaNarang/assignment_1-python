from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

# Input birth year from the user
try:
    birth_year = int(input("Enter your birth year: "))
    if birth_year > datetime.now().year:
        print("Please enter a valid birth year.")
    else:
        age = calculate_age(birth_year)
        print(f"You are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a valid year.")