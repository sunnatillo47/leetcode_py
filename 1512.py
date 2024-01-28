class Solution:
    def numIdenticalPairs(self, nums):
        xxx = set(nums)
        count = 0
        if len(nums) == len(xxx):
            return 0
        else:
            for n in range(len(nums)):
                for k in range(n+1, len(nums)):
                    if nums[n] == nums[k]:
                        count += 1
                    
        return count