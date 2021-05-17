"""
File: test_link_sort.py
Author: sxn6531@g.rit.edu  Steven Ng
Language: Python3
Description: This file imports link_sort.py and calls functions from that file to run the main and read_file function.
"""

from link_sort import *

def read_file(filename):
    """
    This function takes a data file and turns it into a sequence in the order of the file.
    :param filename:
    :return:
    """
    fd = open(filename)
    lst = None
    for line in fd:
        lst = Node(int(line.strip()) , lst)
    fd.close()
    lst = reverseRec(lst)
    return lst

def main():
    """
    This function runs all the fuctions in a single call.
    :return:
    """
    x = input("Enter File Name: ")
    if x == "":
        return
    else:
        lsn = read_file(x)
        if lsn == None:
            return
    print("unsorted: ", lsn)
    sorted = link_sort(lsn)
    print("sorted: " , sorted)
    print("pretty print original: ")
    pretty_print(lsn , "")
    print("pretty print sorted: ")
    pretty_print(sorted , "")

main()