# Author: Matthew Neufeld
# Program Description: Creates the SrabbleDict class from data in scrabble5.txt
# Collaborators/References: https://www.kite.com/python/answers/how-to-check-if-a-string-contains-certain-characters-in-python


class ScrabbleDict:

    def __init__(self, size, filename):
        """Initializes each parameter and creates the dictionary
        Parameters: self, size, filename
        returns: N/A
        """

        self.filename = filename
        self.dict1 = {}
        self.size = size

        # creating the dictionary with each line from file as a key and value
        file = open(self.filename, 'r')
        for line in file:
            new_line = line.strip('\n')
            # validating that the length of each word is the proper size
            if len(new_line) == self.size:
                self.dict1[new_line.upper()] = new_line.upper()
        file.close()

    def create_key_list(self):
        """Function creates a list of all keys in the word dictionary
        Parameters: self
        returns: key_list
        """

        # every key in self.dict1 will be added to key_list
        key_list = []
        for key in self.dict1:
            key_list.append(key)

        return key_list

    def check(self, word):
        """Function determines whether a word is in the word dictionary or not
        Parameters: self, word
        returns: True or False
        """

        # function will return True if the word is self.dict1 - False otherwise
        if word in self.dict1:
            return True
        else:
            return False

    def get_size(self):
        """Function gets the number of keys in the word dictionary
        Parameters: self
        returns: len(self.dict1.keys())
        """

        return len(self.dict1.keys())

    def get_words(self, letter):
        """ Function returns a list of all keys in a dictionary that begin with a given letter
        Parameters: self, letter
        returns: sorted_list
        """

        word_list = []
        for key in self.dict1:
            if key[0] == letter:  # key[0] evaluates to the first letter of the key
                word_list.append(key)

        # ensures that the contents of the list is sorted
        # method description from assignment: "returns a sorted list of words in the dictionary starting with the character letter"
        sorted_list = sorted(word_list)
        return sorted_list

    def get_word_size(self):
        """Function gets the length of the words in the word dictionary
        Parameters: self
        returns: len(list(self.dict1)[0])
        """

        # because all words in the dictionary are the same length, any index can be used. I chose index = 0
        # need to use list() because dictionaries cannot be indexed
        return len(list(self.dict1)[0])

    def get_masked_words(self, template):
        """Function takes a template with wildcard(s) ('*') and returns a list of words that the target_word could be
        based on the unmasked words and position of the wildcard(s)

        Parameters: self, template
        returns final_list
        """

        # following chunk of code generates template_list: a list of all characters from the template and index_list: --
        # a list of the indexes of wildcards
        template_list = []
        index_list = []
        for item in range(len(template)):
            # adding every template item to template_list
            template_list.append(template[item])
            # adding the index of every '*' to index_list
            if template[item] == '*':
                index_list.append(item)

        # following chunk of code creates a list of lists of letters from all words in the word dictionary
        # making a key_list from the word dictionary
        key_list = self.create_key_list()
        list_of_list_letters = []
        for key in key_list:
            letter_list = []
            for letter in key:
                # adding each letter in the word to letter_list
                letter_list.append(letter)
            # taking each resulting letter_list and add it to list_of_list_letters
            list_of_list_letters.append(letter_list)

        # this chunk of code replaces each letter in each list in list_of_list_letters with a wildcard based on --
        # index_list - result is a list containing lists with wildcards in the same index(es) as template
        for i in index_list:
            for a_list in range(len(list_of_list_letters)):
                list_of_list_letters[a_list][i] = '*'

        # this chunk of code compares each list in list_of_list_letters with template list - if they are equal, then --
        # original unmasked version of that word is added to final_list and is returned
        final_list = []
        for index in range(len(list_of_list_letters)):
            # comparing 2 lists with wildcards
            if list_of_list_letters[index] == template_list:
                # adding unmasked version of the word to final_list if equal
                final_list.append(key_list[index])

        return final_list

    def get_constrained_words(self, template, letters):
        """Function works similarly to get_unmasked_words except it returns a list of all words that could be the
        target word given indicated letters - extended from get_unmasked_words

        Parameters: self, template, letters
        returns constrained_words
        """

        constrained_words = []
        bool_lists = []
        for word in template:
            # letter_match_list is a list of bool values - if the letter in the word in the template is one of the ch --
            # in letters, then that index is True - otherwise False.
            letter_match_list = [letter in letters for letter in word]
            bool_lists.append(letter_match_list)

        # this chunk counts up the number of times True occurs in each list - if the count of True is equal to length --
        # of the letters, then the same index of the template is added to constrained words
        for index in range(len(bool_lists)):
            if bool_lists[index].count(True) == len(letters):
                constrained_words.append(template[index])

        return constrained_words


def main():

    # TESTING ScrabbleDict methods

    dict1 = ScrabbleDict(5, 'scrabble5.txt')

    # Testing the create_key_list method
    print(dict1.create_key_list())

    # Testing the check method
    print(dict1.check('ACHOO'))
    print(dict1.check('MATTHEW'))

    # Testing the get_size method
    print(dict1.get_size())

    # Testing the get_words method
    print(dict1.get_words('A'))

    # Testing the get_word_size method
    print(dict1.get_word_size())

    # Testing the get_masked_words methods
    print(dict1.get_masked_words('T**ER'))

    # Testing the get_constrained_words methods
    template = dict1.get_masked_words('TI*E*')
    print(dict1.get_constrained_words(template, ['R']))


if __name__ == "__main__":
    main()