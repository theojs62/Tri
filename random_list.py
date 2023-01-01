import random #This module help us to use random objects.

def int_random_list(number_of_element=random.randint(1, 1000)) : #Initializing the function which generate a list with random integers.
    f_list = [] #Creating the future list with those random numbers.
    for i in range(number_of_element) : #A loop executed an unknown number of time.
        f_list.append(random.randint(1, 1000)) #Adding a random integer to the list.
    return f_list #Show the list.

def float_random_list(number_of_element=random.randint(1, 1000)) : #Initializing the function which generate a list with random floating numbers.
    f_list = [] #Creating the future list with those random numbers.
    for i in range(number_of_element) : #A loop executed an unknown number of time.
        f_list.append(random.uniform(1, 1000)) #Adding a random floats to the list.
    return f_list #Show the list.

def random_list(number_of_elements : int) -> list :
    """
    This function generate a random list with the length of number_of_element
    Args:
        number_of_elements (int) : This is the number of elements
    Return:
        generated_list (list) : This is the generated random list
    """
    generated_list = []
    for i in range(number_of_elements) :
        generated_list.append(random.randint(0, 5000))
    return generated_list