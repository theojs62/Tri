#!/usr/bin/python3

import random, time, matplotlib, selection, random_list, quicksort, pile_sort, merge_sort, insertion, check_sorted_list, bubble_sort


def execution_time_calculating(module_name : str, number_of_elements_in_list : int) -> float :
    """
    This function can measure the time the computer needs to do a sort.
    Args:
        module_name (str) : This is the name of the module
    Return:
        time_execution (float) : This is the time the computer needs to do a sort
    """
    times = []
    for i in range(20) :
        f_list = random_list.random_list(number_of_elements_in_list)
        t1 = time.time()
        if module_name == "insertion" : insertion.insertion_sort(f_list, False)
        elif module_name == "selection" : selection.selection_sort(f_list)
        elif module_name == "bubble_sort" : bubble_sort.bubbleSort(f_list, False)
        elif module_name == "merge_sort" : merge_sort.merge_sort(f_list, False)
        elif module_name == "quicksort" : quicksort.quicksort(f_list)
        elif module_name == "pile_sort" : pile_sort.trier(f_list)
        times.append(time.time() - t1)
    # Making the average
    sum = 0
    for t in times :
        sum += t
    return sum/len(times)


print(execution_time_calculating("pile_sort", 50000))
