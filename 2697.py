class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = [i for i in s]
        for n in range(len(s)):
            s[-(n+1)] = s[n]

        return s

#2697
# 80.8%
