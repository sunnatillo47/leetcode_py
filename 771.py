class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        arr = [i for i in jewels]
        count = 0
        for n in stones:
            if n in arr:
                count += 1
        
        return count