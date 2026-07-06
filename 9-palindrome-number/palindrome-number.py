class Solution(object):
    def isPalindrome(self, x):
        s= str (x)
        rev =""

        for i in s :
            rev = i + rev 

        return s == rev 
        