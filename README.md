# Adventure game

## Table of Contents

* [Project Description](#project_description)
* [Project Specification](#project_specification)
* [Contributing](#contributing)
* [Code Description](#code_description)

## Project Description

 This project is a simple version of an old-fashioned text-based adventure game. 

- The game gives players a description of what's happening, and then asks them to make a choice.
- Multiple print statements, as they get displayed in the terminal should slow up wth short delay after each line.
- Something different happens depending on the choice the player made.
- The game also includes some random factors, so that it's a little different each time.
- The game has conditions for winning and losing.
When the game is over, it asks if the player wants to play again.


## Project Specification 


- Output text to the console.
Descriptions are printed to the console for the player to see.

- Import modules and use functions from those modules.
The time.sleep function is used to create delays between messages so that they aren't all printed at once.
The random.choice or random.randint function is used to influence the game so that each game is different in some way.

- Use the input function in combination with conditional statements (e.g., if and while) to create an interactive program.
    - The input function is used to ask the player what they would like to do.

    - The player's choices affect what happens in the game, including:

        - Whether the player wins or loses
        - Whether to restart or exit after the game is over

- Use a conditional loop to handle invalid input.
    - If the player enters a choice that is not valid, the game gives them the chance to retry until they enter a valid option.
    - The game does not crash and does not treat invalid input as a valid choice.

- Refactor code by defining and calling functions.

    - The code includes at least four function definitions that are used to improve the code in some way, such as by:

        - Reducing repetition
        - Reducing complexity
        - Improving the readability or organization of the code
    - Each function should have a single purpose and a name that describes that purpose.

- Write code that follows the standard Python style guide.
The pycodestyle tool reports zero errors and zero warnings.

- Test code and produce an error-free program.
The program is a playable game, and runs from start to finish without crashing or displaying errors.



## Contributing

The script.js Python code works in comand console. to start a game open GIT BASH, print: "python adventure_game_Valentina_Olekhnovich". Don't forget to change directory mit cd- comand on directory where you coped a file.

## Code Description
Use time module and the time.sleep function. This will cause a 1-second delay after the print statement.

```
import time
```

```
def print_pause(print_text):
    print(print_text)
    time.sleep(1)
```
Use random.choice function to influence the game so that each game is different in some way.
```
import random
```

```
    enemy_list = ['dog', 'elephant', 'tiger', 'monkey', 'octopus',
                  'robot', 'unicorn', 'vampire', 'Freddie Mercury']
    enemy = random.choice(enemy_list)
```    
The code includes several function definitions that are used to improve the code in some way.

- greetings()
- villa(enemy, items)
- greetings_in_forest(enemy, items)
- def forest(enemy, items)
- def rock(enemy, items)
- def choice_wrong_answer(choice)
- def play_again()
- def choose()
- def start_game()


In play_again function used lower(), which returns a copy of a string, entered by user, in which all characters are lowercase
``` 
def play_again():
    play_again_choice = input("Would you like to play again? ").lower()
    if play_again_choice == "no":
        print_pause("FINISH")
    elif play_again_choice == "yes":
        choose()
    else:
        print_pause("Sorry, I don't understand you, plese answer yes or no")
        play_again()
``` 


The pycodestyle tool use to check errors and warnings.

