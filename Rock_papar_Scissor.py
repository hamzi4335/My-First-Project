import random

item_list = ["Rock","Papar","Scissor"]
user_choice = input("Enter your move (Rock,Papar,Scissor) : ")
comp_choice = random.choice(item_list)

print(f"User_Choice = {user_choice}  Computer_choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same : Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Papar":
        print("Papar covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = you win")

elif user_choice == "Papar":
    if comp_choice == "Scissor":
        print("Scissor cuts papar = Computer Win")
    else:
        print("Paper covers rock = You win")

elif user_choice == "Scissor":
    if comp_choice == "Papar":
        print("Scissor cuts papar : You win")
    else:
        print("Rock smashes Scissor : Computer WIN")