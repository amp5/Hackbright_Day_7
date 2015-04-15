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
        item_c = word_list[index + 2]
        #item_c = word_list[index + 2] <- this is the third instance. The other group used 
        #.get to check and append the list section of the dictionary...
        

        print item_b
    
        if index < (len(word_list) - 3):
            key_value = (item_a, item_b)
            value_list = [item_c]
            # do an if statement, if it is there already, append the list. 
            #If it is not there in list, create new list
            
            if not key_value in word_dict:
               word_dict[key_value] = [item_c]
            else:
               value_list = value_list + (item_c)
            #value_list.append(item_c)
          
            #word_dict[key_value] = value_list

            print key_value
            

        else:
            print "I'm done."
            break
    print word_dict
    

"""
for statement looks through out txt file using the dict keys as unique identifiers
every time the for loop finds a matching pair, the loop will take the next word (the third word) 
append the list associated with that uniue key

check: print dict
"""


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
