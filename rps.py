from random import randint
t=["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
while player == False:
    player= input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie, BORING")
    elif player == "Rock":
        if computer == "Paper":
            print ("You lost dumbass!", computer, "covers", player)
        else:
            print("You got lucky", player, "fucks up", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("L NERD!", computer , "cuts up", player)
        else:
            print ("You won", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print ("LMFAO LLLLLLL", computer, "fucks up", player)
        else:
            print ("Good shit buddy.", player, "snips up", computer)
    else:
        print ("You spelled something wrong dumb dumb. Try again")
computer = t[randint(0,2)]
player = False