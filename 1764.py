class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n = len(groups)
        i = 0
        
        for group in groups:
            found = False
            while i < len(nums) - len(group) + 1:
                if nums[i:i+len(group)] == group:
                    found = True
                    break
                i += 1
            
            if not found:
                return False
            i += len(group)
        return True