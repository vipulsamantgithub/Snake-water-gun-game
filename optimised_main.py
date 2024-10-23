import random
computer=random.choice([1,0,-1])

count_c=0
count_u=0
round=0
while (count_c<3 and count_u<3):
    user=int(input("Enter your choice: "))
    dict={ 1:"Gun",0:"Water",-1:"Snake" }

    print(f"Your choice was:{dict[user]}  \n Computer choose:{dict[computer]}")

    if (computer==user):
        print("It's a draw!")
    else:
        if (computer-user)==-1 or (computer-user)==2:     # We are evaluating two expressions (computer - user == -1) and (computer == 2), which is simpler.
            round+=1
            print(f"You lost round {round}! Computer Wins!")
            count_c+=1
            
        else:
            round+=1
            print(f"You won round {round}! Computer lost!")
            count_u+=1
       

if count_u==3:
    print("Congratulations! You won.")
    print(f"You won in {round} rounds.")
else:
    print("Computer won!")
    print(f"Computer won in {round} rounds.")
    print("It was a tough rounds. Let's play again.")
