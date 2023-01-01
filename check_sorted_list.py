#!/usr/bin/python3

#THIS FUNCTION ALLOW US TO MAKE A SELECTION SORT
def check_sorted_list(f_list) : #We write "f_" to avoid the confusion with the keyword "list" of python language
    #We make a loop which allow us to see if an element is bigger than the next one
    for i in range(len(f_list) - 1) :
        if f_list[i] > f_list[i + 1] : return False
    return True