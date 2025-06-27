print("Welcome to my Computer quiz!")

playing = input("Do you want to play the Quiz? ")

if playing.lower() != "yes":
    quit()

print("Ok let's play :)")
score = 0

#Question 1
answer = input("What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Question 2
answer = input("What is the full form of GPU? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Question 3
answer = input("What is the full form of RAM? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Question 4
answer = input("What is the full form of ROM? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


#Question 5
answer = input("What is the full form of PSU? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions right!")
print("You got " + str((score/5)*100) + "%.")




