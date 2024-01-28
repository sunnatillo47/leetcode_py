class Solution(object):
    def runningSum(self, nums):
        new_arr = []
        arr_len = len(nums)
        for n in range(1, arr_len+1):
            c = 0
            for i in range(n):
                c += nums[i]
            new_arr.append(c)

        return print(new_arr)
            
obj = Solution()
obj.runningSum([3,1,2,10,1])

