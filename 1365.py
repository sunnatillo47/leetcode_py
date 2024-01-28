class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        new_arr = []
        arr_len = len(nums)
        
        for n in range(arr_len):
                c = 0
                for h in nums:
                    if nums[n] > h:
                        c += 1
                new_arr.append(c)
                c = 0

        return print(new_arr)

obj = Solution()
obj.smallerNumbersThanCurrent([6,5,4,8])
                        