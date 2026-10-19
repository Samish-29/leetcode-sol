class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        r = []
        for i in range(len(nums)):
            if nums[i] == target:
                r.append(i)
        return r