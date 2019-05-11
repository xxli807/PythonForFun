#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        for i in range(n):
            seen = set()
            for j in range (i, n):
                if (s[j] in seen):
                    break
                seen.add(s[j])
            longest = max(len(seen), longest)
        
        return longest
        

