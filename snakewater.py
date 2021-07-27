import random
from os import system

def Play_Game():
    print("--------Welcome To Our Game Snake Water Gun!--------")
    print("Some Rules :-")
    print("1. If you will choose Snake and Computer will choose water then you will get 1 point")
    print("2. If you will Gun and Computer will choose Snake Then you will get 1 point")
    print("3. You will get 10 chances to Complete the Game")
    print("Are you Ready to Play!! press 1 to start the Game")
    start = int(input())

    if start == 1:
        system('cls')
        i = 1
        user_point = 0
        comp_point = 0
        while i <= 10:
            print("1. Snake\n2. Water\n3. Gun")
            user_choice = int(input())

            comp_choice = random.randint(1, 3)

            if comp_choice == 1:
                print("Computer's Choice Snake")

            elif comp_choice == 2:
                print("Computer's Choice Water")

            elif comp_choice == 3:
                print("Computer's Choice Gun")

            if user_choice == 1 and comp_choice == 2:
                user_point += 1

            elif user_choice == 2 and comp_choice == 1:
                comp_point += 1

            elif user_choice == 1 and comp_choice == 3:
                comp_point += 1

            elif user_choice == 3 and comp_choice == 1:
                user_point += 1

            elif user_choice != 1 and user_choice != 2 and user_choice != 3:
                print("Invalid Choice try again")
                exit()

            print("Your Score", user_point, "\t",
                  "Computer's Score", comp_point)
            print("Chances remaining", 10-i)

            if i == 10:
                if user_point > comp_point:
                    print("Congratulations You Win!!")
                    print("Press 0 to exit:")
                    exit1 = int(input())

                    if exit1 == 0:
                        exit()

                elif comp_point > user_point:
                    print("You Lose! Better Luck next time")
                    print("Press 0 to exit:")
                    exit1 = int(input())

                    if exit1 == 0:
                        exit()

                elif comp_point == user_choice:
                    print("Game has been draw!")
                    print("Press 0 to exit:")
                    exit1 = int(input())

                    if exit1 == 0:
                        exit()

            if i != 10:
                print("Press any key to continue....")
                cont = input()
                if cont:
                    system('cls')
            i = i + 1

    else:
        print("Ok We will meet next time")

Play_Game()

