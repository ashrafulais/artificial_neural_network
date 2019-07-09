'''
Rock beats scissors
Scissors beats paper
Paper beats rock
'''

while(True):
    a1 = input("player1: ")
    a2 = input("player2: ")

    if a1==a2:
        print("no one wins")
    elif a1=="rock":
        if a2=="scissors":
            print("rock wins")
        else:
            print("paper wins")

    elif a1=="scissors":
        if a2=="paper":
            print("scissors wins")
        else:
            print("rock wins")
            
    elif a1=="paper":
        if a2=="scissors":
            print("scissors wins")
        else:
            print("paper wins")

    else:
        print("Incorrect input found.")
        
    if input("play again? ") != "yes":
        print("program terminated.")
        break
        
    
