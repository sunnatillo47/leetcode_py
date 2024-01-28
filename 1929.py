class Solution:
    def getConcatenation(self, nums):
        
        for n in range(len(nums)):
        	nums.append(nums[n])

        return nums