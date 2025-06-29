import random 
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_exp():

    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + operator + str(right)
    answer = eval(expr)
    return expr,answer

print("Press enter to start the game!")
print("------------------------------")

start_time = time.time()

for i in range(10):
    expr,answer = generate_exp()
    while True:
        guess = input("Problem #"+str(i+1)+": "+expr+" = ")
        if guess == str(answer):
            break

end_time = time.time()
total_time = round(end_time-start_time,2)

print("------------------------------")
print("Nice work! You finished in", total_time, "seconds!")
        



