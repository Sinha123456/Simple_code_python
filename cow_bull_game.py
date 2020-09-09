import random
def compare_num(num, user_guess):
    cow_bull = [0,0]
    for i in range(len(num)):
        if num[i] == user_guess[i]:
            cow_bull[1]+=1
        else:
            cow_bull[0]+=1
    return cow_bull
if __name__=="__main__":
    play = True
    num = str(random.randint(0,9999))
    guesses = 0
    print("Let's play a game of cowbull")
    print("I will generate anumber , and you have to guess the number one digit at a time")
    print("For every number in the wrong place, you will get a cow unless bull")
    print("The game ends when you get 4 bulls")
    print("Type exit at any prompt to exit.")
    while play:
        user_guess = input("Give me your best guess")
        if user_guess == "exit":
            break
        cowbull_count = compare_num(num, user_guess)
        guesses+=1
        print("You have" + str(cowbull_count[0]) + "cows and " + str(cowbull_count[1]) + "bulls")
        if cowbull_count == 4:
            play = False
            print("you win the game after " + str(guesses) + "The number was" + str(num))
            break
        else:
            print("your guess wasn't quite right, try again")
