from random import randint

print("Hello Traveller ! Welcome to the game of guesses ")
name = input("What is your name : ")
print("Hi ", name, " Would you like to play the game of guesses (Enter Yes/No)")
high_score = 11
while True:
    wish = input()
    if wish.lower() == 'yes':
        print("**     ******  ******  ******       ******  *****     |")
        print("**     **        **    **           **      **  **    |")
        print("**     ****      **    ******       **  **  **  **    |")
        print("**     **        **        **       **  **  **  **    |")
        print("****** ******    **    ******       ******  ******    * \n\n")
        if high_score == 11:
            print("There is currently no high score, its yours for taking")
        else:
            print("Current highscore is ", high_score, " attempts")
        a = randint(1, 10)
        b = 0
        score = 0
        while a != b:
            try:
                b = int(input("pick a number between 1 to 10 \n"))
            except ValueError:
                print("!!!!Please enter a number between 1 to 10!!!!\n\n")
            if a > b:
                print("its Higher")
            elif a < b:
                print("its lower")
            score = score + 1
        print("Nice ! you got it \nIt took you ", score, "attempts")
        print("Would you like to play again ( Enter Yes/No")
        if high_score > score:
            high_score = score
    elif wish.lower() == 'no':
        print("That's cool, have a good one!")
        break
    else:
        print("Please Enter Yes/No")
