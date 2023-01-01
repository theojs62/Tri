#!/usr/bin/python3
import random 

#Function for insert sort .
def insertion_sort (L, accurate=True):
    #variable N for list size .
    N = len(L)
    # a loop that goes from 1 to N
    for n in range(1,N):
        #Comparision of elements 
        b= L[n]
        j = n-1
        # a loop 
        while j>=0 and L[j] > b :
            L[j+1] = L[j] # make a shift to put another elements 
            j = j-1
        L[j+1] = b
        if(accurate):
            print("Etape ", j+ 1, " : ", L)
    return L