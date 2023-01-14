# Author: Matthew Neufeld
# Program Description: Implementation of the Wordle game
# Collaborators/References: https://realpython.com/python-counter/,
# https://www.youtube.com/watch?v=JapurB9UCSg


import random
from Wordle175 import ScrabbleDict


def get_target(dict1):
    """Function generates the target word that the user tries to guess.
    Parameters: dict1
    returns: target_word
    """

    # using random.choice() allows to pick a random word from the key list created by dict1.create_key_list() -- this
    # random word will be stored as target word
    target_word = random.choice(dict1.create_key_list())

    return target_word


def get_guess(attempt_num, dict1, guessed_words):
    """Function prompts user to enter in a guess. Function also makes sure that the entered guess is valid.
    Parameters: attempt_num, dict1, guessed_words
    returns: guess
    """

    # valid_guess is initially set to false. Loop will not end until valid guess is entered and valid_guess = True
    valid_guess = False
    while not valid_guess:
        # attempt_num is updated in main() when a valid guess is entered
        # .upper() is used to meet display requirements
        guess = input(f'Attempt {attempt_num}: Please enter a five-letter word: ').upper()

        # checking if the length of guess does not exceed the word size
        # dict1.get_word_size() = 5
        if len(guess) > dict1.get_word_size():
            print(f'{guess} is too long')
        elif len(guess) < dict1.get_word_size():
            print(f'{guess} is too short')

        # guess must be in the dictionary to be valid
        elif not dict1.check(guess):
            print(f'{guess} is not a recognized word')

        # no repeat guesses - therefore guess_words is relevant and guess cannot be in guessed_words to be valid
        elif guess in guessed_words:
            print(f'{guess} has already been guessed')

        # if no issue is raised, the guess will be returned and valid_guess = True so the loop will end
        # the valid guess is also stored in guess_words so it cannot be guessed again
        else:
            guessed_words.append(guess)
            valid_guess = True
            return guess


def formatting(colour):
    """Function takes the colour lists and alters them to meet display requirements.
    Parameters: colour
    returns: colour
    """

    # although colour may look like set, it is not. It is a list converted to a string made to look like a set
    # sorted(colour) ensures that letters within the list are sorted alphabetically
    colour = str(sorted(colour))
    colour = colour.replace('[', '{')
    colour = colour.replace(']', '}')
    colour = colour.replace("'", '')

    return colour


def create_letter_list(word):
    """Function takes a word and makes a list containing all of its letters.
    Parameters: word
    returns: letter_list
    """

    # every letter in the particular word wil be added to letter_list
    letter_list = []
    for letter in word:
        letter_list.append(letter)

    return letter_list


def letter_counting(word):
    """Function takes word and counts each occurrence of the letter within the word. Results are stored in a dictionary.
    Parameters: word
    returns: letter_count
    """

    letter_count = {}
    for letter in word:
        # initialize each letter in the word with a value of 0
        if letter not in letter_count:
            letter_count[letter] = 0
        # +1 is added to the value of the letter every time the letter appears in the word
        letter_count[letter] += 1

    return letter_count


def letter_enumeration(letter_count, letter_list):
    """Function enumerates letters in a word based on how many times they appear in the word.
    Parameters: letter_count, letter_list
    returns: letter_list
    """

    # num_letter_list will contain all letters that have been enumerated
    num_letter_list = []

    for key in letter_count:
        # letters that only appear in a word once are left alone
        if letter_count[key] > 1:

            # the following chunk of code performs the enumeration
            # x is just a variable that takes on the enumeration value
            # letter[key] is the amount of times a letter occurs in the word - it determines the extent of the numbering
            # +1 is added in the range to turn for example: E, E1 --> E1, E2
            for x in range(1, letter_count[key] + 1):
                # key is the letter - it is concatenated with the enumeration value and added to num_letter_list
                numbered_letter = key + str(x)
                num_letter_list.append(numbered_letter)

                # the following chunk of code performs the replacement of non-numbered letters with numbered letters
                for replace_letter in range(len(letter_list)):
                    for num_ch in num_letter_list:
                        # at this point, only keys with >1 occurrences can be accessed, if a letter in letter_list is
                        # the same as a key, then it must be replaced by ch, which is the enumerated letter
                        if letter_list[replace_letter] == key:
                            letter_list[replace_letter] = num_ch
                            # num_ch is popped from the list during each ch assignment to ensure that a num_ch is not --
                            # assigned more than once
                            num_letter_list.pop()

    # updated letter_list is returned with enumerated values (if letters occur multiple times)
    return letter_list


def feedback(guess, target_word):
    """Function provides feedback to the user based on how guess relates to target word. If a letter in the guess is in
    Green, it means the letter is in the target word and in the right position. If a letter is in Orange, it means the
    letter is in the target word, but not in the right position. If a letter is in Red, it means that the letter is not
    in the target word.

    Parameters: guess, target_word
    returns: None
    """

    green = []
    orange = []
    red = []

    # creating letter lists for guess and target_word
    guess_letter_list = create_letter_list(guess)
    target_letter_list = create_letter_list(target_word)

    # counting all the letters in guess and target_word
    guess_letter_counter = letter_counting(guess)
    target_letter_counter = letter_counting(target_word)

    # enumerating each letter in guess and target_word
    guess_letter_list = letter_enumeration(guess_letter_counter, guess_letter_list)
    target_letter_list = letter_enumeration(target_letter_counter, target_letter_list)

    for guess_letter in range(len(guess_letter_list)):

        # letters will only be added to green if the non-numbered letter in the same position for each list are equal
        if guess_letter_list[guess_letter][0] == target_letter_list[guess_letter][0]:
            green.append(guess_letter_list[guess_letter])

        # if the letter is only in the target list than it goes into orange
        # checking guess_letter_list[guess_letter][0] in target_word to account for guesses with no repeating letters
        elif guess_letter_list[guess_letter] in target_letter_list or guess_letter_list[guess_letter][0] in target_word:
            # ensures that user isn't misled by multiple guess letters being in orange when there is only one of the --
            # guess_letter in the word
            if target_letter_counter[target_letter_list[guess_letter][0]] < guess_letter_counter[guess_letter_list[guess_letter][0]]:
                red.append(guess_letter_list[guess_letter])
            else:
                orange.append(guess_letter_list[guess_letter])

        # every other letter (letters not in the target word) go into red
        else:
            red.append(guess_letter_list[guess_letter])

    # giving feedbacks proper display requirements
    green = formatting(green)
    orange = formatting(orange)
    red = formatting(red)

    print(f'{guess} Green={green} – Orange={orange} – Red={red}')


def main():

    # establishing the dictionary
    dict1 = ScrabbleDict(5, 'scrabble5.txt')

    # getting the target word
    target_word = get_target(dict1)

    # guessed words is initially empty and will have valid guesses after each attempt
    guessed_words = []

    # win is initially set to False - it will be become True if the player guesses the target word
    win = False
    attempt_num = 1
    guess_limit = 6

    while attempt_num <= guess_limit and not win:  # loop will run until guess_limit is reached or player wins
        # getting the player's guess
        guess = get_guess(attempt_num, dict1, guessed_words)

        # feedback will be displayed for each guess on every attempt
        for guess in guessed_words:
            feedback(guess, target_word)

        attempt_num += 1

        # player wins:
        if guess == target_word:
            win = True
            print(f'Found in {attempt_num} attempts. Well done. The Word is {target_word}')

    # player loses:
    if not win:
        print(f'Sorry you lose. The Word is {target_word}')


if __name__ == "__main__":
    main()