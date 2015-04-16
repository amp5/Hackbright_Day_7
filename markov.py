
from sys import argv
from random import choice



class SimpleMarkovGenerator(object):

    def read_file(self, filename):
     

        opened_filename = open(filename)
        read_filename = opened_filename.read()
        return read_filename

    def make_chains(self, read_filename):
        """Takes input text as string; returns dictionary of markov chains."""


        word_list = read_filename.split()

        word_dict = {}

        for index in range(len(word_list)-2):
            key = (word_list[index], word_list[index + 1])
            value = word_list[index + 2]

            if key not in word_dict:
                word_dict[key] = []
            word_dict[key].append(value)


        return word_dict
        
    # """
    # for statement looks through out txt file using the dict keys as unique identifiers
    # every time the for loop finds a matching pair, the loop will take the next word (the third word) 
    # append the list associated with that uniue key

    # check: print dict
    # """

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""
        
        
        key = choice(chains.keys())
        
        key_str = key[0] +" " + key[1]

        while key in chains:
            next_one = choice(chains[key])
            key_str = key_str + " " + next_one
            key = (key[1], next_one)
   
        return key_str

    # Change this to read input_text from a file, deciding which file should
    # be used by examining the `sys.argv` arguments (if neccessary, see the
    # Python docs for sys.argv)


if __name__ == "__main__":
    script, filename = argv

    print argv


    instance = SimpleMarkovGenerator()


    #### NNED TO MAKE THIS PART PRINT ME THE MARKOV GENERATOR!
    chain_dict = instance.make_chains(instance.read_file(filename))

    random_text = instance.make_text(chain_dict)

    #print chain_dict
    print random_text

