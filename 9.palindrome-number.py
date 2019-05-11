#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        length = len(strX)
        if length == 1:
            return True
        else:
            # n = int(strX[::-1])
            # if(abs(n) > (1 << 31) - 1):
            #     return False
            reversedStr = strX[::-1]
            if (strX == reversedStr): 
                return True
            
            return False

