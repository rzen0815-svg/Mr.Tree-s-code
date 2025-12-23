import random


def theguess():
    return int(input("Make a guess: "))

def compare_with_answer(guess,answer1):
    if guess==answer1:
        return "equal"
    elif guess<answer1:
        return "low"
    else:
        return "high"


def difficulty():
    while True:
        di=input("Choose a difficulty.Type 'easy' and 'hard'")
        if di in ["easy","hard"]:
            return di
        print("Invaild input")

def lifes(difficult):
    if difficult=="hard":
        print("You have 5 attempts remaining to guess the number.")
        return 5
    else:
        print("You have 10 attempts remaining to guess the number.")
        return 10


def game():
    game_over=False
    while not game_over:
        answer=random.randint(1,100)
        difficult=difficulty()
        life=lifes(difficult)
        while life>0:
            guess=theguess()
            result=compare_with_answer(guess,answer)
            if result=="equal":
                print("You win")
                break
            else:
                print(f"Too {result}")
                life-=1
        if life==0:
            print("You've run out of guesses,you lose.")


        a=input("This repl has exited,run again? 'yes' or 'no'")
        if a =="yes":
            game_over=False
        else:
            game_over=True


game()


