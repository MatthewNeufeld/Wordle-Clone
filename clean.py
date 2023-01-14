# Author: Matthew Neufeld
# Program Description: Creates scrabble5.txt from corrupted Word5Dict.txt file
# Collaborators/References:


def new_file(filename):
    """Function takes a corrupted word file and produces a new file with each word by itself on its own line
    Parameters: filename
    returns: None
    """

    file = open(filename, 'r')
    # .readlines() turns the data into a list
    corrupted = file.readlines()
    file.close()
    all_words = []
    # items in corrupted are chunks of words with #, so use split method to make each word its own item - separating --
    # at each # character
    for chunk in corrupted:
        word_list = chunk.split('#')
        for word in word_list:
            # removing the newline character and adding each cleaned word to the all_word list
            new_word = word.strip('\n')
            all_words.append(new_word)

    # ensuring that there are no blank items in the all_words list
    if '' in all_words:
        all_words.remove('')

    scrabble5 = open('scrabble5.txt', 'w')
    for index in range(len(all_words)):
        # prevents the creation of a blank line at the very end
        if index == len(all_words) - 1:
            scrabble5.write(all_words[index])
        # ensures that every word is on its own line
        else:
            scrabble5.write(all_words[index] + '\n')


def main():

    new_file('word5Dict.txt')


if __name__ == "__main__":
    main()