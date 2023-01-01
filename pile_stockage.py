#!/usr/bin/python3

def initPile():
    """
    Function to initialize the pile.\n
    Return:
        an empty list
    """
    return []

def estVide(pile:list):
    """
    Returns a boolean to check if the pile is empty.\n
    Args:
        pile (list) : Our pile is a list.
    Return:
        A boolean.
    """
    return pile == []

def empiler(pile:list, n:int):
    """
    This process can add an element to the pile.\n
    Args:
        pile (list) : The pile is represented by a list.
        n (int) : n is the element.
    """
    pile.append(n)


def depiler(pile:list):
    """
    Remove the last element who entered into the pile.\n
    Args:
        pile (list) : Our pile is a list.
    """
    pile.pop()


def sommet(pile:list):
    """
    This is the top of the pile, if it is not empty.\n
    Args:
        pile (list) : Our pile is a list.
    Returns:
        The last element of the pile, or nothing if the pile is empty.
    """
    if(not estVide(pile)): return pile[-1]
