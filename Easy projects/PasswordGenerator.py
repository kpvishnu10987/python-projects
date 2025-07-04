import random 
import string

def password_generator(min_length , numbers = True , special_char = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False 

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        if new_char in special:
            has_special = True
        
        meets_criteria = True

        if numbers:
            meets_criteria = has_numbers
        if special_char:
            meets_criteria = meets_criteria and has_special
    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers in password?  (y/n) : ").lower() == "y"
has_special = input("Do you want to have special characters in password?  (y/n) : ").lower() == "y"

pwd = password_generator(min_length , has_number , has_special)
print(pwd)