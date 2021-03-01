#!/usr/local/bin/python3
import time
import random
item = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.5)


# intro to what is happening
def intro():

    print_pause("A scary monster controls the city gates")
    print_pause("To get out of the city, you have to either defeat the monster"
                "in combat or answer his silly riddles correctly")
    print_pause("Those who don't win in either tasks become the monster's"
                "supper")
    while True:
        option = int(input("Enter 1 for riddle or 2 for combat: "))
        if option in [1, 2]:
            return option
        else:
            print_pause("Enter the correct option")


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


def combat():

    print_pause("You get ready to fight the monster ")
    find_sword = input("Do you have a sword? Type yes or no ").lower()

    if "yes" in find_sword:
        print_pause("You slash the monster and escape")
    else:
        print_pause("You have forgotten to bring your sword to fight")
        print_pause("You are defeated. Monster will be having you for his "
                    "supper")


if __name__ == '__main__':

    while True:
        output_intro = intro()
        if output_intro == 1:
            riddle()
        else:
            combat()
        play_again = input("Would you like to play again? (yes / no) ").lower()

        if play_again == 'no':
            break
