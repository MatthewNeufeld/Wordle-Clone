# Author: Matthew Neufeld
# Program Description: Provides hints to the user on what the target word could be
# Collaborators/References:


from Wordle175 import ScrabbleDict


def get_letter_count(word_list):
    """Function counts every occurrence of each letter in the complete word dictionary
    Parameters: word_list
    returns: sorted(letter_count.items())
    """

    # function is similar to letter_counting() in main.py, except it takes a list as a parameter and returns a tuple
    # word_list is a list of all the words in the dictionary based off scrabble5.txt

    letter_count = {}
    for word in word_list:
        for letter in word:
            if letter not in letter_count:
                # initializing each letter with a value of 0
                letter_count[letter] = 0
            # +1 is added to the value of the letter every time the letter appears in the list
            letter_count[letter] += 1

    # sorted(letter_count.items()) is a list of alphabetically sorted tuples consisting of a letter and its number of --
    # occurrences
    return sorted(letter_count.items())


def display_stats(letter_count):
    """ Function displays a letter and its number of occurrences, the frequency of the letter (in percentage), and a
    histogram that aids in visualizing how often a particular letter occurs in the dictionary.

    Parameters: letter_count
    returns: None
    """

    # summing all letters in the dictionary
    all_letters = 0
    for a_tuple in letter_count:
        all_letters += a_tuple[1]  # a_tuple[1] evaluates to the number of occurrences of a particular letter

    # displaying the stats of each letter
    # a_tuple[0] evaluates to the particular letter
    for a_tuple in letter_count:
        print(f'{a_tuple[0]}: {str(a_tuple[1]).rjust(4)} {str(round(float((a_tuple[1] / all_letters) * 100), 2)).rjust(5)}% {int(round(((a_tuple[1] / all_letters) * 100))) * "*".ljust(1)}')


def get_wildcard_list(template):
    """Function gets the wildcards ('*') from a template and stores them in a list.
    Parameters: template
    returns: wildcard_list
    """

    # code will traverse through the template, if it finds a wildcard, it will add it to wildcard_list
    wildcard_list = []
    for wildcard in template:
        if wildcard == '*':
            wildcard_list.append(wildcard)

    return wildcard_list


def main():

    # establishing the dictionary
    dict1 = ScrabbleDict(5, 'scrabble5.txt')

    # getting the list of all words in the dictionary
    word_list = dict1.create_key_list()
    # getting the number of occurrences for each letter
    letter_count = get_letter_count(word_list)
    # displaying the stats of each letter
    display_stats(letter_count)

    # PROVIDING HINTS:

    # prompting user to enter a template and getting wildcard_list
    template = input('Enter template: ').upper()
    wildcard_list = get_wildcard_list(template)

    # validating that the length of the template is the same size as the length of words in the dictionary
    if len(template) == dict1.get_word_size():
        # prompting user to enter letters if they want extended hints - optional, enter 1 if extended hints not wanted
        letters = list(input('Enter capital letters that could replace wildcards for extended hints. Enter 1 if you do not want extended hints: '))
        if letters == ['1']:
            # shows user a list of all words that could be the target word
            print(dict1.get_masked_words(template))
        # validating that there are not more wildcards than letters
        elif len(letters) < len(wildcard_list):
            # shows user a list of all words that could be the target word given the indicated letters
            template1 = dict1.get_masked_words(template)
            print(dict1.get_constrained_words(template1, letters))


if __name__ == "__main__":
    main()