import time
import random


def print_pause(print_text):
    print(print_text)
    time.sleep(1)


def greetings():
    print_pause("You sailed on a huge luxury cruise ship.")
    print_pause("Suddenly the sky turned black, high waves rose,"
                " an evil wind blew.")
    print_pause("Your eyes have darkened and you don’t remember anything.")
    print_pause("You found yourself on a desert island.")
    print_pause("You see a modern villa, but it is all braided by vines "
                "and looks abandoned. ")


def villa(enemy, items):
    if "sword" in items:
        print_pause("You slaughtered the {} with a sword and survived. "
                    "Now you can stay to live in a villa.\n"
                    " --GAME OVER--".format(enemy))
        play_again()
    elif "guitar" in items:
        print_pause("You tried to sing to the {}, but it did not increase"
                    " your chances of survival.\n --GAME OVER--".format(enemy))
        play_again()
    elif "mobile phone" in items:
        print_pause("You called 911 and was saved. Hooorey!")
        play_again()
    elif "refrigerator" in items:
        print_pause("You made a trap from the refrigerator and saved."
                    " Hooorey!")
        play_again()
    elif "gun" in items:
        print_pause("You killed {} and survived. Hooorey!".format(enemy))
        play_again()
    else:
        print_pause("You were eaten by a {} who lives in an abandoned villa. "
                    "Sorry!\n --GAME OVER--".format(enemy))
        play_again()


def greetings_in_forest(enemy, items):
    print_pause("You hid in the forest and saw a hungry wild {} emerge"
                " from the villa, it seems he considers the villa"
                " to be his home.".format(enemy))
    print_pause("What would you preffere to do?")


def forest(enemy, items):
    forest_choice = input("Please enter 1 or 2 \n "
                          "1. You will stay in forest.\n "
                          "2. You will climb a rock.\n")
    if forest_choice == '1':
        print_pause("You died in the forest without food and water."
                    "\n --GAME OVER--")
        play_again()
    elif forest_choice == '2':
        print_pause("Very good")
        rock(enemy, items)
    else:
        print_pause("Sorry, I don't understand you.")
        forest(enemy, items)


def rock(enemy, items):
    print_pause("You climbed a rock to explore the island.")
    magical_item_list = ['sword', 'guitar', 'mobile phone',
                         'refrigerator', 'gun']

    magical_item = random.choice(magical_item_list)
    if magical_item in items:
        print_pause("You allready have a {}, there is nothing "
                    "more to explore.".format(magical_item))
    else:
        items.append(magical_item)
        print_pause("You took a {}.".format(magical_item))
    print_pause("You go back to the villa.")
    villa(enemy, items)


def choice_wrong_answer(choice):
    print_pause("Sorry, I don't understand you")
    choose()


def play_again():
    play_again_choice = input("Would you like to play again? ").lower()
    if play_again_choice == "no":
        print_pause("FINISH")
    elif play_again_choice == "yes":
        choose()
    else:
        print_pause("Sorry, I don't understand you, plese answer yes or no")
        play_again()


def choose():
    enemy_list = ['dog', 'elephant', 'tiger', 'monkey', 'octopus',
                  'robot', 'unicorn', 'vampire', 'Freddie Mercury']
    enemy = random.choice(enemy_list)
    items = []

    choice = input("Please enter 1 or 2 or 3\n 1. You will enter the villa.\n "
                   "2. You hide in the forest.\n 3. "
                   "Сlimb a rock to explore the island.\n ")
    if choice == '1':
        villa(enemy, items)
    elif choice == '2':
        greetings_in_forest(enemy, items)
        forest(enemy, items)
    elif choice == '3':
        rock(enemy, items)
    elif choice != '1' and choice != '2' and choice != '3':
        choice_wrong_answer(choice)


def start_game():
    greetings()
    choose()


start_game()
