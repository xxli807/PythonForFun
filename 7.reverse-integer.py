#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strX = str(x)
        length = len(strX)
        if length == 1:
            return x
        else:
            firstChar = strX[0]
            lastChar = strX[length-1]

            if firstChar == "-":
                subStrx = strX[1:length]
                if lastChar == "0":
                    subStrx = strX[1:length-1]
                reverseSub = subStrx[::-1]
                return "-" + reverseSub
            else:
                if lastChar == "0":
                    subStrx = strX[0:length-1]
                    return subStrx[::-1]
                else:
                    return strX[::-1]
