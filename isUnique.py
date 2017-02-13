"""
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures
"""
import sys
import array

def isUnique( string ):
    a = array.array('i', (0 for i in range(0, 127)))
    for value in string:
        if a[ord(value)] == 1:
            return False
        a[ord(value)] = 1
    return True

def printMe(string):
    print('isUnique : ' + str(isUnique(string)))
    return

"Test Cases"
printMe('abcdefghsssjkl')
printMe('1231312412412')
printMe('absjkls')
printMe('abcdjkl')
printMe('abcd')
