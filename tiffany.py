# your code goes here
from sys import argv
import random

script, rest_filename = argv

opened_restaurant_ratings_filename = open(rest_filename)
read_restaurant_ratings_file = opened_restaurant_ratings_filename.read()


def dictionary_of_restaurant_ratings():
    '''
    The first split separates the document into strings at the new line character,
    which is at the end of each "line" between the number ratings and the first 
    letter of the next restaurant name
    '''
    line_break_list_of_str = read_restaurant_ratings_file.split("\n") 
    '''
    next, creating an empty list in which I will add two item tuples 
    in order to create the dictionary 
    '''
    tuple_restaurant_and_ratings_list = []
    for item in line_break_list_of_str: #this for loop will iterate through the list of strings of restaurant names and ratings with a colon in between
        restaurant_rating = item.split(":") #for each string, a new list will be created by spliting at the colon
        tuple_restaurant_and_ratings_list.append((restaurant_rating[0], restaurant_rating[1])) #appending to the empty list a two element tuple with the rest name and rest rating
    
    restaurant_dictionary = dict(tuple_restaurant_and_ratings_list) #turning the list of tuples into a dictionary
    for dict_tuple in restaurant_dictionary.items(): #for each tuple in the dictionary items,
        print "%s is rated at %s." % dict_tuple #print the following phrase using the string format -- this is what the entire function returns
    
    user_restaurant_key = raw_input("Please input a new restaurant to rate: ") #Prompt the user for restaurant name and set it equal to a variable for a key
    restaurant_dictionary[user_restaurant_key] = int(raw_input("On a scale from 1-5, how would you rate this restaurant? ")) 
    # the above step is prompting user for rating, convert to integer, and bind to the value for the restuarant key; 
    # this step is also adding this item to the dictionary

    # iterating over the keys in the sorted dictionary and printing the item (restaurant name) and the corresponding value (rating)
    for item in sorted(restaurant_dictionary):
        print item, restaurant_dictionary[item]
    #
    #last part -- working on the updates to random restaurant
    # user_name = input("Greetings, user!  What's your name? ")
    # random_restaurant = random.sample(restaurant_dictionary)


dictionary_of_restaurant_ratings() #calling the function!