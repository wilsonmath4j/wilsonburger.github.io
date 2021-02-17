from random import randint
#Establish the Rules of the Game
print("Player A gets a point each time all three players match.")

print("Player B gets a point each time two of the three players match.")

print("Player C gets a point each time none of the players match.")
#Asks what role the user wants to play
role = input("Which player do you want to be? Please enter A, B, or C.")

if role == "A":
    other1 = "B"
    other2 = "C"

if role == "B":
    other1 = "A"
    other2 = "C"
    
if role == "C":
    other1 = "A"
    other2 = "B"

#create a list of play options
t = ["Rock", "Paper", "Scissors"]
r = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer1
computer1 = t[randint(0,2)]

#assign a random play to the computer2
computer2 = r[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    print("Player", role, "picked", player)
    print("Player", other1, "picked", computer1)
    print("Player", other2, "picked", computer2)
    if player == computer1 and player == computer2:
        print("3-way Tie! Player A gets a point.")
    
    elif player == computer1 and player != computer2:
        print("2 matching! Player B gets a point.")
    
    elif player == computer2 and player != computer1:
        print("2 matching! Player B gets a point.")
        
    elif computer2 == computer1 and player != computer2:
        print("2 matching! Player B gets a point.")
        
    elif player != computer1 and player != computer2 and computer1 != computer2:
        print("No matches! Player C gets a point.")
   
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer1 = t[randint(0,2)]