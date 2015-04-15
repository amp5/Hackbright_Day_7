import sys

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""


    word_list = open(corpus).read().split()

    #print word_list

    word_dict = {}
    
    #counter = 0
    for index in range(len(word_list)):
        item_a = word_list[index]
        item_b = word_list[index + 1]
        #item_c = word_list[index + 2] <- this is the third instance. The other group used 
        #.get to check and append the list section of the dictionary...
        print item_a

        print item_b
        if index < (len(word_list) - 2):
            key_value = (item_a, item_b)
            #counter = counter + 1
            #print counter
            word_dict[key_value] = []
            print key_value


        else:
            print "I'm done."
            break


    # for index, item in enumerate(word_list):

    #     if index == (len(word_list) - 2):
    #         print "I'm at the end"
    #         break
    #     else: 
    #         print "I am not at the end yet."
    #         # key_value = (item[index -2 ]) #item[index + 1])

    # print key_value 
    #         #testvariable = word_dict[(item[index], item[index + 1],)] 
                 
                 

#TUPLE = (ITEM1[INDEX],ITEM2,)
    print word_dict




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
