# Number challenge

This Number challenge game was made purely with python code, the user has 15 attempts to guess a randomly generated 3 digit number.

The computer will tell you if your are higher or lower to give the user a good chance

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


## Testing 

-  Due to the nature of the project testing has been conducted throughout its entirety, mainly through the use of running the program in the terminal and ensuring i get the output intended. Evidence of this is clear within my commits, with various debugs recorded. 

-  Various sections of code where also developed in isolation and outputs checked before being inserted into the running order as the size of the project grew.  

-  Once at the finished point, limit testing has been conducted by myself and my peers on slack through the peer-code-review channel, there is currently no reported issues that cause the game to break.

## **Validator Testing

    - Python
        - No errors were found when passing through the [PEP8 Validator tool](http://pep8online.com/)


## Unfixed Bugs 

-  The only bug i was unable to fix, due to not being able to replicate it, was an issue with how the board display was printed out to the terminal. My only instance of this bug was just after i utilized my updated legend. Once the guess board was printed out again on the next turn the display discrepancy wasn't present.

![bug](/assets/images/glitch.png)

[Return to Table of Contents](#contents)

## Deployment 

- The site is deployed via Heroku. The steps to deploy are as follows:

    *Ensure the requirements for the project are added to the requirements.txt file prior to deployment*

    1: From the dashboard, select New and then Create new app.
    
    2: Enter an individual app name into the text box, select a region from the dropdown and then press Create app.
    
    3: A Heroku app has now been created and the Deploy tab is opened.
    
    4: Select the Settings tab.
    
    5: If required, click on the Reveal Config Vars button and add.
    
    6: In the Buildpacks section of the settings tab, click on Add Buildpack, select Python and then save changes.
    
    7: Click on Add Buildpack again, select node.js and then save changes.

    *When they are on the dashboard, ensure that python is above node.js on the list*
    
    8: Open the Deploy tab.
    
    9: In the deployment method section, select GitHub and confirm the connection.
    
    10: Enter the repo-name into the text box. When the correct repo appears, click Connect.
    
    11: If desired, in the Automatic deploys section, click Enable Automatic Deploys.

    *This then updates the deployment every time GitHub code is pushed.*
    
    12: To complete the process click on the Deploy Brach button in the Manual deploy section. 
        
    *This will take a few seconds to complete while Heroku builds the app.*
    
    13: A message will appear informing you that the app was successfully deployed and a View button will bring you to the live site.

The live link can be found here - [ULTIMATE BATTLESHIPS](https://ultimate-battleships-lewiscm.herokuapp.com/)

## Credits 

* Thanks to the Code Institute tutor support team, who helped me develop my understanding throughout this project.  

- **Content** 

    * Various highlighted sections of my code are developed from this [YouTube Tutorial.](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=223s&ab_channel=KnowledgeMavens) However, my project is object orientated, with several extra features, so in most instances the base code has been padded out or accepts different arguments.

    * My use of the re library was based of this post on [Stack Overflow.](https://stackoverflow.com/questions/57062794/how-to-check-if-a-string-has-any-special-characters/57062899)

    * My table of contents in the readme was developed from this post on [Stack Overflow.](https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents)  

- **Media**

    * None Required.


