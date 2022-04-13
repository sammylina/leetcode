#!/usr/bin/env python3

def palindrome(x: int) -> bool:

    orig = x
    rev = 0
    if x < 0: 
        return False
    while orig:
        rev = (rev * 10) + (orig % 10)
        orig = orig // 10
        
    return x == rev

def palindrome_iterate(x: int) -> bool:
    """iterate over the array of element from two
    direction
    """
    s = str(x)
    left_i = 0
    right_i = len(s) - 1
 
    while (left_i < right_i):
        if s[left_i] != s[right_i]:
            return False
        left_i += 1
        right_i -= 1
            
    return True
