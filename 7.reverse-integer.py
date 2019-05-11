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
        
        # try:
        #     int(x)
        # except:
        #     return 0

        strX = str(x)
        length = len(strX)
        if length == 1:
            return x
        else:
            firstChar = strX[0]
            lastChar = strX[length-1]
            # remove the 0 at the end
            strX = strX.rstrip("0")

            if firstChar == "-":
                subStrx = strX[1:length]
                if lastChar == "0":
                    subStrx = strX[1:length-1]
                reverseSub = subStrx[::-1]
                n = int(reverseSub)
                if(abs(n) > (1 << 31) - 1):
                    return 0
                return "-" + reverseSub
            else:
                if lastChar == "0":
                    subStrx = strX[0:length-1]
                    return subStrx[::-1]
                else:
                    n = int(strX[::-1])
                    if(abs(n) > (1 << 31) - 1):
                        return 0
                    return strX[::-1]
