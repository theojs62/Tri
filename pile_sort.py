#!/usr/bin/python3
from pile_stockage import *

def trier(pile : list, accurate: bool = False) -> list:
    """
    This function is made for sorting a pile with 
    the help of a third pile.\n
    Args:
        pile (list) : This is a list, based on a pile, unsorted
    Return:
        B  (list) : This is the sorted list
    """
    A = pile
    B = initPile()
    C = initPile()
    #Creating 3 piles, A, B and C, the two lasts are empty. 
    while not estVide(A) or not estVide(C):
        #While A and C are not empty.
        if(estVide(A)): #If A is empty.
            while not estVide(C):
                elementC = sommet(C)
                depiler(C)
                empiler(A, elementC)
            #Exchanging values from C to A.
            elementA = sommet(A)
            depiler(A)
            empiler(B, elementA)
            #Putting the last element of A in B.
        else:
            if(estVide(B)):#if B is empty.
                elementA = sommet(A)
                depiler(A)
                empiler(B, elementA)
                #Putting the last element of A in B.
            else:
                if(sommet(A) > sommet(B)): 
                    #If the top of A is bigger than the top of B.
                    elementB = sommet(B)
                    depiler(B)
                    empiler(C, elementB)
                    #Putting the last element of B in C.
                    elementA  = sommet(A)
                    depiler(A)
                    empiler(B,  elementA)
                    #Putting the last element of A in B.
                else:
                    elementA = sommet(A)
                    depiler(A)
                    empiler(C, elementA)
                    #Putting the last element of A in C.
            if(accurate): #If we choose more accuracy from the function.
                print("State of the pile before it is sorted : {} \n".format(B))
                #Showing the state of the pile.
    return B #So the output will be the sorted pile.
