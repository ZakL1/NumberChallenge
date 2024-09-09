import random



def start():
    """
    Explanation of the game
    """
    print("The computer will generate a 3 digit number for the user to guess.\n")
    print("The computer will notify the user if a digit is correct.\n")
    print("The program will end if the user does not guess the number correctly after 5 guesses.\n")


def generate_random_number():
    """
    The computer will generate a 3 digit number for
    the user the guess
    """
    print(random.randint(100,999))




def main():
    """
    Run all functions
    """
    start()
    generate_random_number()




main()