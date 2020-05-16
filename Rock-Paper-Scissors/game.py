import random
name = input("Enter your name: ")
print("Hello,", name)
rating = 0
inputs = input().split(",")
if inputs == ['']:
    inputs = ["rock", "paper", "scissors"]
print("Okay, let's start")
files = open("rating.txt", "r")
new_rating = []
for line in files.readlines():
    if line.split()[0] == name:
        rating = int(line.split()[1].rstrip())
    else:
        new_rating.append(line)
game_rules={}
for i in range(len(inputs)):
    game_rules[inputs[i]] = inputs[i+1:i+len(inputs) // 2 + 1] if i <= len(inputs) // 2 \
        else inputs[i+1:] + inputs[:i-len(inputs)//2]
while True:

    player_choice = input()
    if player_choice == "quit":
        print("Bye!")
        break
    if player_choice == "rating":
        print("Your rating:", rating)
        continue
    if player_choice not in inputs:
        print("Invalid input")
        continue
    computer_choice = random.choice(inputs)
    if player_choice == computer_choice:
        print("There is a draw ({}).\nRating(+50)\n".format(computer_choice))
        rating += 50
    elif computer_choice in game_rules[player_choice]:
        print("Sorry, but computer chose {}.\nRating(-50)\n".format(computer_choice))
        rating -= 50
    else:
        print("Well done. Computer chose {} and failed.\nRating(+100)\n".format(computer_choice))
        rating += 100
files.close()
files = open("rating.txt", "w")
new_rating.append(name + " " + str(rating))
files.writelines(new_rating)
files.close()