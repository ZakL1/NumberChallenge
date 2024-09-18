import random

computer_number = (random.randint(100,999))
counter = 0


def start():
    """
    Explanation of the game
    """
    print("The computer will generate a 3 digit number for the user to guess.")
    print("The computer will notify the user if a digit is correct.")
    print("The program will end if the user does not guess the number correctly after 5 guesses.\n")


def generate_random_number():
    """
    The computer will generate a 3 digit number for
    the user the guess
    """
    print(computer_number)


def guess_number():
    """
    User inputs a guess, computer then responds
    """
    print("Guess must be 3 digits.")
    print("There should not be any spaces inbetween digits.\n")

    guess_int = input("Guess here:\n")

    return guess_int


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
        if (int(guess_int) == computer_number):
            print('Congratulations you win!')
            print('It took you' + str(counter) + 'guesses')
        else:
            print('Not quite, have another guess!')
            guess_int = input("Guess here:\n")
        
    

 




def main():
    """
    Run all functions
    """
    start()
    generate_random_number()
    values = guess_number()
    validate_answer(values)
    check_answer(values)




main()