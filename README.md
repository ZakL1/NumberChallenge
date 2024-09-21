# Number challenge

This Number challenge game was made purely with python code, the user has 15 attempts to guess a randomly generated 3 digit number.

The computer will tell you if your are higher or lower to give the user a good chance

[Live version of my site](https://number-challenge1-b5b37897af65.herokuapp.com/)

![readme hero image](/assets/images/image.png)


## Existing Features 

- **The Welcome Message**

    * When a new game starts the rules are explained.

    * The player is then asked to take a guess

![The Welcome Message](/assets/images/project3guess.png)

- **Correct guess and play again**

    * Once guess is correct the game will ask you if you want tom play again and will tell you how many guesses it took

    * The program says to play again press y or to stop press any other key


![Correct guess](/assets/images/correctguess.png)

- **Incorrect guess**

    * If you guess incorrectly the game will tell you if the number you guessed is higher or lower than the computers number, this is to make it easier 
    for the player to narrow the answer down


![Incorrect guess](/assets/images/incorrectguess.png)

## Future Features 

- **Challenge**

    * In the future I would add different difficulties for the user to choose from, these would entail the user to guess a larger number or a smaller
    number with less guesses or more guesses depending on the difficulty


## Testing 

-  Testing was carried out as I completed the project 

-  1 major bug I had was the users guess not being converted into an integer but I managed to fix it with the help of a tutor

-  Another simple bug I had was needing to reset the counter when the play replayed the game, the reason it wasn't resetting was
because I declared the counter variable globally. Once I removed the variable globally and had it inside the corect function it reset everytime.

-  To test if my code was working I would constantly use print statements to make sure I was getting the correct output.


## **Validator Testing

    - Python
        - The main errors I had were having 3 lines spacing between my functions so I removed 1 empty line as needed

        - Currently no errors in the [PEP8 Validator tool](https://pep8ci.herokuapp.com/)


## Unfixed Bugs 

-  The only bug I haven't fixed is when the user guesses a number below or over 3 digits it counts as a guess but it doesn't count as a guess
if the user inputs a string. The reason I didn't fix this is because I ran out of time sadly.


## Deployment 

- The site is deployed via Heroku. The steps to deploy are as follows:

   - Create an account with Heroku

   - Create a new Heroku app

   - Go to the deploy tab and add Python and NodeJS buildpacks

   - Link the Heroku app to the GitHub repository

   - Deploy the branch manually

## Credits 

* Thanks to the Code Institute tutor support team, who helped me develop my understanding throughout this project.  

- **Content** 

    * The validate_answer() function I used was taken from the lovesandwiches project

- **Media**

    * None Required.


