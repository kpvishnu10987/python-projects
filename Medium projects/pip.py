import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter the no of players: (2-4) ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid,Try again.")
    
max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", players_score[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Do you like to roll (y): ").lower()

            if should_roll != 'y':
                break

            value = roll()
            if value == 1:
                print("Bad Luck! you got a one.")
                current_score = 0
                break
            else:
                current_score += value
                print("You got a:",value)
            
            print("Your current score is:",current_score)
        players_score[player_idx] += current_score
        print("Your total score is:",players_score[player_idx])

max_score = max(players_score)
winning_idx = players_score.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)
        
