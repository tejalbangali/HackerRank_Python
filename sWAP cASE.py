link --> https://www.hackerrank.com/challenges/swap-case/problem


#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description

# Complete the swap_case function in the editor below.
# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format
# A single line containing a string .

# Constraints
# 0 < len(s) <= 1000

# Sample Input 0
# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".


#Solution 1 :
def swap_case(s):
    s=s.swapcase()
    return s
    
s = input()
result = swap_case(s)
print(result)


#Solution 2 :
def swap_case(s):
    new=''
    for i in range(len(s)):
        if(s[i].islower()):
            new+=s[i].upper()
        elif(s[i].isupper()):
            new+=s[i].lower()
        else:
            new+=s[i]
    return(new)

swap_case('hIiI')
