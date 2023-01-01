#!/usr/bin/python3
import random 
#Function for merge sort 
def merge_sort (list, accurate=True) :
    if len(list) > 1 :
        middle= len(list)//2 #take half the list
        G = list[:middle] 
        D = list[middle:]
        #DIVISION
        merge_sort(G)
        merge_sort(D)
        #sort the two list
        t=[] # created two list 
        r=[]
        while G:
            mini=G[0] # add an element to the list G
            for z in G:
                if z < mini: #we look at each element in relation to the new 
                    mini=z
            G.remove(mini) # delete element mini
            r.append(mini) # add element new 
        while D:
            mini=D[0] # add an element to the list G
            for z in D:
                if z < mini: #we look at each element in relation to the new 
                    mini=z
            D.remove(mini)# delete element mini
            t.append(mini)# add element new 
        list_full=[] # created list 
        for i in range(len(r)): # deux buckle 
            for j in range(len(t)) : 
                if r[i]> t[j] :
                    list_full.append(t[j]) # add an elements list_full 
                else :
                    list_full.append(r[i]) #add an element list_full 
                    break
        return list_full 