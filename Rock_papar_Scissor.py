import random

item_list = ["Rock","Papar","Scissor"]
user_choice = input("Enter your move (Rock,Papar,Scissor) : ")
comp_choice = random.choice(item_list)

print(f"User_Choice = {user_choice}  Computer_choice = {comp_choice}")

if user_choice == comp_choice:
        print("Both chose the same: Match Tie!")
elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers Rock: Computer Wins!")
        else:
            print("Rock smashes Scissor: You Win!")
elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("Scissor cuts Paper: Computer Wins!")
        else:
            print("Paper covers Rock: You Win!")
elif user_choice == "Scissor":
        if comp_choice == "Paper":
            print("Scissor cuts Paper: You Win!")
        else:
            print("Rock smashes Scissor: Computer Wins!")
