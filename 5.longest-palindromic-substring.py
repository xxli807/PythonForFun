#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        text = s.lower()
        length = len(text)
        if length == 1:
            return text

        results = []

        for i in range(length):
            for j in range(0, i):
                chunk = text[j:i + 1]

                if chunk == chunk[::-1]:
                    results.append(chunk)
        
        if len(results) != 0:
            return results[0]
        return ''
