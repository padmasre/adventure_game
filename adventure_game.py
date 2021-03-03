#!/usr/local/bin/python3
import time
import random


# print message with time delay
def print_pause(message_to_print, pause=1):
    print(message_to_print)
    time.sleep(pause)


# check if user is passing the right value
def check_valid_input(for_1, for_2):
    while True:
        option = input(f"Enter 1 for {for_1} or 2 for {for_2}: ")
        try:
            option = int(option)
            if option in [1, 2]:
                return option
            else:
                print_pause("Enter the correct option")
        except ValueError:
            print_pause("Enter the correct option")


# intro to what is happening
def intro():

    print_pause("A scary monster controls the city gates")
    print_pause("To get out of the city, you have to either defeat the monster"
                "in combat or answer his silly riddles correctly")
    print_pause("Those who don't win in either tasks become the monster's "
                "supper")

    valid_input = check_valid_input(for_1='riddle', for_2='combat')

    return valid_input


# execute the riddle scenario
def riddle():

    print_pause("You think you are very clever.")
    print_pause("You should use only 1 word to answer my riddles.")

    list_of_riddles = [
        {'question': 'What has a face and two hands, but no arms or legs?',
         'answer': 'clock'},
        {'question': (
          'I start out tall, but the longer I stand, the shorter I grow. '
          'What am I?'),
         'answer': 'candle'},
        {'question': 'How many months have 28 days?', 'answer': 'all'}]

    riddle_dict = random.choice(list_of_riddles)

    riddle = riddle_dict['question']

    answer = riddle_dict['answer']

    response = input(riddle + '\n')

    if response.lower() == answer.lower():
        print_pause("You are free to go")
    else:
        print_pause("You gave an wrong answer")
        print_pause("You are my dinner today")


# execute the combat scenario
def combat():

    list_of_options = [
            "You have a sword but it is very blunt. Monster kills you",
            ("You think you had sword but that is a wooden stick."
             " Monster will have you for dinner"),
            "You slash the monster and escape"
            ]

    print_pause("You get ready to fight the monster.Do you have a sword? ")
    valid_input = check_valid_input(for_1='yes', for_2='no')

    if valid_input == 1:
        print_pause(random.choice(list_of_options))
    else:
        print_pause("You have forgotten to bring your sword to fight")
        print_pause("You are defeated. Monster will be having you for his "
                    "supper")


# Check if user wants to play again
def play_again():

    print_pause("Would you like to play again?")

    valid_input = check_valid_input(for_1='playing again', for_2='exit')

    if valid_input == 1:
        return True
    else:
        return False


if __name__ == '__main__':

    play = True
    while play:
        # presenting intro to user
        output_intro = intro()

        # calling scenario based on user choice
        if output_intro == 1:
            riddle()
        else:
            combat()

        play = play_again()
