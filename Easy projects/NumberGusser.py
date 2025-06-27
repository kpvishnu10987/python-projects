import random

top_of_range = input("Type a top_limit to the range of numbers: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter an number greater than 'zero' next time")
        quit()
else:
    print("Please enter a number next time")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_input = input("Guess the number: ")
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Please enter a number.")
        continue

    if user_input == random_number:
        print("You got it!")
        break
    elif user_input > random_number:
        print("You are above the number!")
    else:
        print("You are below the number!")
    
    
print("you got it in",guesses,"guesses")
    
    