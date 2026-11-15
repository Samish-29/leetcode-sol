class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            if max(nums[:i+1]) - min(nums[i:]) <= k:
                return i
        return -1
