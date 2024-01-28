
class Solution(object):
    def twoSum(self, nums, target):
    	l = len(nums)
    	for n in range(l):
    		for i in range(l):
    			if nums[n] + nums[i] == target:
    				print(f"{n} va {i} indexlar")
    			else:
    				print("Bunday sonlar mavjud emas")





obj = Solution()
obj.twoSum([2,7,1,15], 18)