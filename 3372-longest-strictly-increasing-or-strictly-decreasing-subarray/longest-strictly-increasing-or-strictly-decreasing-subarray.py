class Solution(object):
    def longestMonotonicSubarray(self, nums):
        i = d = ans = 1

        for a, b in zip(nums, nums[1:]):
            i = i + 1 if b > a else 1
            d = d + 1 if b < a else 1
            ans = max(ans, i, d)

            
        return ans