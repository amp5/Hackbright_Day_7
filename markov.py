import sys

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""


    word_list = open(corpus).read().split()

    #print word_list

    seuss_dictory_no_values = {}

    for item in word_list:
        seuss_dictory_no_values[(word_list[word_list.index(item)], word_list[word_list.index(item) + 1])] = []

    print seuss_dictory_no_values




make_chains("green-eggs.txt")
    # string_into_list = []

    # for line in open_file:
    #     line = line.split('\n')
    #     for item in line:
    #         word = item.split(" ")
    #         string_into_list.append(word)
    # print string_into_list
        # line = line[0]
        # for word in line:
        #     string_into_list.append(word[0])
        # print string_into_list
        #txt_file_string.append(line)

    #print txt_file_string


#def make_text(chains):
  #  """Takes dictionary of markov chains; returns random text."""

    
    #return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "green-eggs.txt"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# print chain_dict

# Produce random text
# random_text = make_text(chain_dict)

#print random_text
