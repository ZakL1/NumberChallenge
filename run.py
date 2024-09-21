import random

# computer_number = (random.randint(100,999))
counter = 0


def start():
    """
    Explanation of the game
    """
    print("The computer will generate a 3 digit number for the user to guess.")
    print("The computer will notify the user if a digit is correct.")
    print("The program will end if the user does not guess the number correctly after 10 guesses.\n")



def generate_random_number():
    """
    The computer will generate a 3 digit number for
    the user the guess
    """
    global computer_number
    computer_number = (random.randint(100,999))
    print(computer_number)



def guess_number():
    """
    User inputs a guess, computer then responds
    """
    while True:
        print("Guess must be 3 digits.")
        print("There should not be any spaces inbetween digits.\n")

        guess_int = input("Guess here:\n")
        if guess_int.isdigit():
            return guess_int
        else:
            print("Invalid input. Please enter a  number.\n")




def validate_answer(values):
    """
    This function checks if the users guess is a valid answer
    """   
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True



def check_answer(guess_int):
    """
    Checks if answer is correct or how many
    digits are correct
    """
    while (guess_int != computer_number):
        global counter
        counter += 1
        if (counter > 10):
            print('Oh no, you have run out of guesses! Better luck next time')
            restart()
            continue
        elif (int(guess_int) > computer_number):
            print('Not quite, your guess is too high!')
            # guess_int = input("Guess here:\n")
            guess_int = guess_number()
            continue
        elif (int(guess_int) < computer_number):
            print('Not quite, your guess is too low!')
            # guess_int = input("Guess here:\n")
            guess_int = guess_number()
            continue
        else:
            print('Congratulations you win!')
            print('It took you ' + str(counter) + ' guesses')
            break


        
def restart():
    """
    Asks the user if they want to play again
    """
    global replay
    print("Would you like to play again?\n")
    replay = input("Yes or No:\n")
    if (replay == "Yes"):
        main()
    else:
        print("Thank you for playing, goodbye!")
        


def main():
    """
    Run all functions
    """
    start()
    generate_random_number()
    values = guess_number()
    check_answer(values)
    restart()




main()