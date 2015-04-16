

from sys import argv
from random import choice

script, filename = argv

opened_filename = open(filename)
read_filename = opened_filename.read()

def make_chains(read_filename):
    """Takes input text as string; returns dictionary of markov chains."""


    word_list = read_filename.split()

    #print word_list

    word_dict = {}
    
    #counter = 0
    for index in range(len(word_list)-2):
        key = (word_list[index], word_list[index + 1])
        value = word_list[index + 2]
        #item_c = word_list[index + 2] <- this is the third instance. The other group used 
        #.get to check and append the list section of the dictionary...
        
    
        
    
            # do an if statement, if it is there already, append the list. 
            #If it is not there in list, create new list
            
            # if key not in word_dict:
            #    word_dict[key] = [value]
            # else:
            #    value = value + value

        if key not in word_dict:
            word_dict[key] = []
        word_dict[key].append(value)


            #value_list.append(item_c)
          
            #word_dict[key_value] = value_list

            #print key
            

        #else:
         #   print "I'm done."
          #  break
    return word_dict
    print word_dict
    
# """
# for statement looks through out txt file using the dict keys as unique identifiers
# every time the for loop finds a matching pair, the loop will take the next word (the third word) 
# append the list associated with that uniue key

# check: print dict
# """


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

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    
    
    key = choice(chains.keys())
    
    key_str = key[0] +" " + key[1]

    while key in chains:
        next_one = choice(chains[key])
        key_str = key_str + " " + next_one
        key = (key[1], next_one)
        # key_str = "%s %s %s" % (key_str, key[1], next_one)
        
        # result_lst.append(key)

    #print result_lst
    
    
    print type(key_str)
    print key_str

    #final_markov_chain = ' '.join(result_lst)
    #print final_markov_chain
    
  # while 

    # while loop that randomly chooses a key form our dict and then print the key 
    # and the third indexed word and repeats until there are no word combos that we can do

    #return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "green-eggs.txt"

# # Get a Markov chain
chain_dict = make_chains(read_filename)
print chain_dict

# Produce random text
random_text = make_text(chain_dict)

print random_text
