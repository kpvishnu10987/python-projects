name  = input("What is your name: ")
print("welcome",name,"to this adventure!")

answer = input("You are on the dirt road and it has come to an end do you want to turn right or turn left? Type right or left: ").lower()

if answer == "right":
    answer = input("You come to a river.Do you want to walk around it or do you want to swim across it? Type walk or swim: ").lower()

    if answer == "swim":
        print("You swam across and drown.You lose")
    elif answer ==  "walk":
        print("You are exhasted by walking and died.You lose")
    else:
        print("It is not a valid option.You lose")
elif answer == "left":
    answer = input("You are on the bridge.Do you want to cross or head back ? cross/back: ").lower()

    if answer == "back":
        print("You choose the wrong decision.You lose")
    elif answer == "cross":
        answer = input("You have met a stranger.Do you want to talk to him or ignore ? talk/ignore: ")

        if answer == "ignore":
            print("You lose")
        elif answer == "talk":
            print("Stranger gave you gold.You win!")
        else:
            print("It is not a valid option.You lose")
else:
    print("It is no a valid option.You lose")

print("Thank You for trying",name)