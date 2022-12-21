import random
# Game starts with a welcoming message
print("...")
print("...")
print("...")
print("Hi and welcome to Rock Paper and Scissor game! Now, let's start")
print("...")
print("...")
print("...")

# Setting up the wins count for both players
user_wins = 0
cpu_wins = 0
draws = 0

# List to create the pick for both
picks = ["Rock", "Paper", "Scissor"]
# Error message to display in case of wrong input
error_message = "This is not an Accepted input, please don't be a fool"

while True:
    # This is the user pick system
    user_pick = input(
        "Make your choice by typing R for Rock, P for Paper, S for Scissor or Q to quit: ").lower()
    if user_pick == "r":
        user_pick = picks[0]
    elif user_pick == "p":
        user_pick = picks[1]
    elif user_pick == "s":
        user_pick = picks[2]
    elif user_pick == "q":
        break
    elif user_pick not in picks:
        print(error_message)
        continue

 # This is the cpu pick system
    cpu_pick = picks[random.randint(0, 2)]
    print("...")
    print("You picked " + user_pick)
    print("Cpu picked " + cpu_pick)
    print("...")

# Check the winner of the round
    if user_pick == picks[0] and cpu_pick == picks[2]:
        print("...")
        print("You Win!")
        print("...")
        user_wins = user_wins + 1
    elif user_pick == picks[1] and cpu_pick == picks[0]:
        print("...")
        print("You Win!")
        print("...")
        user_wins = user_wins + 1
    elif user_pick == picks[2] and cpu_pick == picks[1]:
        print("...")
        print("You Win!")
        print("...")
        user_wins = user_wins + 1
    elif user_pick == cpu_pick:
        print("...")
        print("It's a Draw!")
        print("...")
        draws = draws + 1
    else:
        print("...")
        print("Computer Wins!")
        print("...")
        cpu_wins = cpu_wins + 1

    continue
print("...")
print("...")
print("You wins " + str(user_wins) + " times")
print("Cpu wins " + str(cpu_wins) + " times")
print("There have been " + str(cpu_wins) + " draws")
print("...")
print("...")
