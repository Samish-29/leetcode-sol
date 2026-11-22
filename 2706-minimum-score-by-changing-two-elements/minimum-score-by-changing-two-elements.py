class Solution(object):
    def minimizeSum(self, nums):

        nums.sort()
        opt1 = nums[-1] - nums[2]
        opt2 = nums[-3] - nums[0]
        opt3 = nums[-2] - nums[1]
        
        return min(opt1, opt2, opt3)