"""
File: link_sort.py
Author: sxn6531@g.rit.edu Steven Ng
Language: Python3
Description: Code takes a file and turns it into a node before sorting it into a new sorted node.
"""

from linked_code import *

def link_sort(lns):
    """
    This function takes a sequence of unsorted numbers and returns a new sequence of sorted numbers.
    :param lns:
    :return:
    """
    sorted_lns = None
    index = 0
    if lns == None:
        print("Cannot sort empty sequence")
    while lns != None:
        value = lns.value
        x = find_min(lns , value)
        lns = min_remove(x , lns)
        sorted_lns = min_insert(sorted_lns , x , index)
        index += 1
    return sorted_lns

def pretty_print(lsn, numbers):
    """
    This function takes a sequence and prints it in a more visually appealing way.
    :param lsn:
    :param numbers:
    :return:
    """
    numbers += str(lsn.value)
    if lsn.rest != None:
        numbers += ", "
        pretty_print(lsn.rest, numbers)
    else:
        print("[", numbers, "]")

def min_remove(x , lns):
    """
    This function removes the desired value from a sequence.
    :param x:
    :param lns:
    :return:
    """
    y = remove(x, lns)
    return y

def min_insert(sorted_lns , x , index):
    """
    This function takes the desired value and inserts it into a designated sequence for the sorted numbers.
    :param sorted_lns:
    :param x:
    :param index:
    :return:
    """
    y = insertAt(index , x , sorted_lns)
    return y

def find_min(lns , value):
    """
    This function takes a sequence and compares the first sequence to every other sequence to find the min number.
    :param lns:
    :param value:
    :return:
    """
    if lns == None:
        return value
    elif value > lns.value:
        return find_min(lns.rest , lns.value)
    elif value <= lns.value:
        return find_min(lns.rest , value)