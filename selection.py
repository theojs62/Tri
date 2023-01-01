#!/usr/bin/python3

def selection_sort(f_list : list, accurate : bool = False) -> list : #We write "f_" to avoid the confusion with the keyword "list" of python language
    """
    This function allow us to make a selection sort.\n
    Args:
        f_list (list) : This is a list which is to sort
        accurate (bool) : Thanks to this param, we can see the details
    Return:
        f_list (list) : This is a list which is sorted
    """
    if accurate :
        for i in range(len(f_list)) : #We make a loop which explore each element of the list
            little_index = i #We create the variable nammed "little_index" which represent the index i of the list
            for j in range(i + 1, len(f_list)) : #We make a loop which assign the smallest value of this list
                if f_list[little_index] > f_list[j] :
                    little_index = j
            #We reeverse the variables
            temp = f_list[little_index]
            f_list[little_index] = f_list[i]
            f_list[i] = temp
            print(f"Étape n°{i + 1} : \t\t\t\t\t{f_list}")
        return f_list #We return the result
    else :
        for i in range(len(f_list)) : #We make a loop which explore each element of the list
            little_index = i #We create the variable nammed "little_index" which represent the index i of the list
            for j in range(i + 1, len(f_list)) : #We make a loop which assign the smallest value of this list
                if f_list[little_index] > f_list[j] :
                    little_index = j
            #We reeverse the variables
            temp = f_list[little_index]
            f_list[little_index] = f_list[i]
            f_list[i] = temp
        return f_list #We return the result