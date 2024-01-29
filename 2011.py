class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        minus = ["--X", "X--"]
        plus = ["++X", "X++"]
        res = 0
        for n in operations:
            if n in minus:
                res -= 1
            else:
                res += 1
        
        return res