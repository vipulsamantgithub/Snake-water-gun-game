# Snake-water-gun game.
"""

The rules of the game Snake Water Gun are: 
Players: Two players choose one of three objects: snake, water, or gun 
Results: The winner is determined by the following outcomes: 
Snake vs. water: The snake wins because it drinks the water 
Water vs. gun: The water wins because the gun drowns 
Gun vs. snake: The gun wins because it kills the snake 
Draw: If both players choose the same object, the result is a draw 

"""

"""

1: Gun
0: Water
-1: Snake

"""

import random
computer=random.choice([1,0,-1])

count_c=0
count_u=0
round=0
while (count_c<3 and count_u<3):
    user=int(input("Enter your choice: "))
    dict={ 1:"Gun",0:"Water",-1:"Snake" }

    print(f"Your choice was:{dict[user]}  \nComputer choose:{dict[computer]}")

    if (computer==user):
        print("It's a draw!")
    else:
        if (computer==-1 and user== 0) or (computer==0 and user==1) or (computer==1 and user==-1):
            round+=1
            print(f"You lost round {round}! Computer Wins!")
            count_c+=1
            
        elif (computer==-1 and user==1) or (computer==0 and user==-1) or (computer==1 and user==0):
            round+=1
            print(f"You won round {round}! Computer lost!")
            count_u+=1
        else:
            print("Some error has came, please play again.")

if count_u==3:
    print("Congratulations! You won.")
    print(f"You won in {round} rounds.")
else:
    print("Computer won!")
    print(f"Computer won in {round} rounds.")
    print("It was a tough rounds. Let's play again.")
