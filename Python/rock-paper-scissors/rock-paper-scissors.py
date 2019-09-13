import random

decision = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}

def choices():
    computer_choice = random.randint(1, 3)
    try:
        your_choice = int(input("Make your choice \n1)Rock\n2)Paper\n3)Scissors\n"))
        print('Your choice is ' + decision[your_choice])
        print('Computer choice is ' + decision[computer_choice])
        if (your_choice == 1 and computer_choice == 3) or (your_choice == 2 and computer_choice == 1) or (your_choice == 3 and computer_choice == 2):
            print('You Win!')
        elif (your_choice == 1 and computer_choice == 2) or (your_choice == 2 and computer_choice == 3) or (your_choice == 3 and computer_choice == 1):
            print('You Lose!')
        elif (your_choice == 1 and computer_choice == 1) or (your_choice == 2 and computer_choice == 2) or (your_choice == 3 and computer_choice == 3):
            print('Draw!')
    except:
        print('Your choice is not number or your choice is not in the range from 1 to 3')

while True:
    choices()
    a = input("Enter '0' to exit from the game or enter any other key to start the game again\n")
    if a == 'exit()':
        break



# computer_choice = random.randint(1, 3)
#     try:
#         your_choice = int(input("Make your choice \n1)Rock\n2)Paper\n3)Scissors"))
#         if your_choice == 1:
#             if computer_choice == 1:
#                 print("Your choice is Rock")
#                 print("Computer choice is Rock")
#                 print("Draw!")
#             elif computer_choice == 2:
#                 print("Your choice is Rock")
#                 print("Computer choice is Paper")
#                 print("You Lose!")
#             elif computer_choice == 3:
#                 print("Your choice is Rock")
#                 print("Computer choice is Scissors")
#                 print("You Win!")
#         elif your_choice == 2:
#             if computer_choice == 1:
#                 print("Your choice is Paper")
#                 print("Computer choice is Rock")
#                 print("You Win!")
#             elif computer_choice == 2:
#                 print("Your choice is Paper")
#                 print("Computer choice is Paper")
#                 print("Draw!")
#             elif computer_choice == 3:
#                 print("Your choice is Paper")
#                 print("Computer choice is Scissors")
#                 print("You Lose!")
#         elif your_choice == 3:
#             if computer_choice == 1:
#                 print("Your choice is Scissors")
#                 print("Computer choice is Rock")
#                 print("You Lose!")
#             elif computer_choice == 2:
#                 print("Your choice is Scissors")
#                 print("Computer choice is Paper")
#                 print("You Win!")
#             elif computer_choice == 3:
#                 print("Your choice is Scissors")
#                 print("Computer choice is Scissors")
#                 print("Draw!")
#         else:
#             print("Your choice should be from 1 to 3")
#     except:
#         print('Your choice is not number')
