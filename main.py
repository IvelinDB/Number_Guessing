from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the user's guess against the actual answer
def answer_check(user_guess, actual_answer, turns):
    """Checks the answer against guess, returning the number of turns they have remaining"""
    if user_guess > actual_answer:
        print("Too high.")
        return turns -1
    elif user_guess < actual_answer:
        print ("Too low.")
        return turns -1
    else:
        return print(f"CONGRATS! You got the number. The answer was {actual_answer}. You had {turns} attempts remaining.")
    


# Functions to ask the user the difficulty
def set_difficulty():
    level = input(f"Choose a difficulty. Type 'easy' for {EASY_LEVEL_TURNS} lives, or 'hard' for {HARD_LEVEL_TURNS} lives:")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    

def game():
    #Randomly choose a number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100. Lets see if you can beat me")
    answer = randint(1, 100)

    # print(f"Pssst, the correct answer is {answer}") code in order to test that everything was working fine. Not that good at guessing numbers :)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number

        guess = int(input("What is you guess:"))

        # Tracking the number of turns and reduce by 1 if they get it wrong
        turns= answer_check(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses, you lose! Better luck next time.")
            exit()
        elif guess != answer:
            print("Guess again.")

game()