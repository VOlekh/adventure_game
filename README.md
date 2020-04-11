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
TB changed
The script.js JavaScript code works with the provided HTML and CSS files. The script.js file is properly linked to the HTML file, and loading the HTML file shows the correct functionality for the application.

## Code Description
TB changed
 Work with file designs.js.


**Description:** 
TB changed
- make clear up grid function, withot this new grid will be added below the old one.
Tipps: the same can be made by Element.innerHTML (or jQuery's .html())


```
function clearGrid(){
    //To remove all children from an element:
    while (table.firstChild) {
      table.removeChild(table.firstChild);
    };
    };
```
_________________________________________________    
Some notes on Markdown

And in that moment I thought to myself: _Did I turn off the stove?_

## This is an h2.

### This is an h3.

You can indicate emphasis with bold, italic, or strikethrough text.

Style	Syntax	Keyboard shortcut	Example	Output
Bold	** ** or __ __	command/control + b	**This is bold text**	This is bold text
Italic	* * or _ _	command/control + i	*This text is italicized*	This text is italicized
Strikethrough	~~ ~~		~~This was mistaken text~~	This was mistaken text
Bold and nested italic	** ** and _ _		**This text is _extremely_ important**	This text is extremely important
All bold and italic	*** ***		***All this text is important***	All this text is important


- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
