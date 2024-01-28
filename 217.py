class Solution(object):
    def containsDuplicate(self, nums):
        c = 0
        while nums:
            num = nums.pop()
            for n in nums:
                if num == n:
                    c += 1
        if c >= 1:
            print("True")
        else:
            print("False")

obj = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
obj.containsDuplicate(nums)

