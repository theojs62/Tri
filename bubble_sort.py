import random


def bubbleSort(vList, accurate=True): #Initializing new function, which is made for 
                        #sorting a list with the help of bubble sort.

    for i in range(len(vList) - 1): #This loop allows us to explore
                                    # each element of the list.

        for j in range(len(vList) - 1): #The instructions in this loop help us to 
                                        #know the biggest number and to put it 
                                        #in the end of the list.

            if(vList[j] > vList[j + 1]): #If the element is bigger than the next one.

                vList[j], vList[j + 1] = vList[j + 1], vList[j] #permute those elements.
        
        if(accurate):

            print("Etape ", i + 1, " : ", vList)
   
    return vList #Show us the sorted list.
