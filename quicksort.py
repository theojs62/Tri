#!/usr/bin/python

def quicksort(list_unsorted : list, accurate : bool = False)  -> list :
    """
    This function allow us to make a quicksort.\n
    Args:
        list_unsorted (list) : This is a list which is to sort
        accurate (bool) : Thanks to this param, we can see the details
    Return:
        list_sorted (list) : This is a list which is sorted

    """
    # If the list have one element, we return the same list
    if len(list_unsorted) > 1 :
        pivot = list_unsorted[0]
        smallests = []
        biggests = []
        equal = []
        # We show the details if accurate is activate
        if accurate :
            print("pivot = ", pivot)
            print("smallests = ", smallests)
            print("biggests = ", biggests)
            print("equal = ", equal)
        for i in range(len(list_unsorted)) :
            if list_unsorted[i] > pivot : biggests.append(list_unsorted[i])
            elif list_unsorted[i] < pivot : smallests.append(list_unsorted[i])
            else : equal.append(list_unsorted[i])
        list_sorted = quicksort(smallests, accurate = accurate) + equal + quicksort(biggests, accurate = accurate) # We call the same function to finish the job
        # We show the details if accurate is activate
        if accurate :
            print("pivot = ", pivot)
            print("smallests = ", smallests)
            print("biggests = ", biggests)
            print("equal = ", equal)
            print("list_unsorted = ", list_unsorted)
            print("list_sorted = ", list_sorted)
        # We return the variable list_sorted
        return list_sorted
    else : return list_unsorted