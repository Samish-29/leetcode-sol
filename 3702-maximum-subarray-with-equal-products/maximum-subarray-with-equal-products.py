from fractions import gcd

class Solution(object):
    def maxLength(self, nums):
        ans = 2
        for i in range(len(nums)):
            p, g, l = 1, nums[i], nums[i]
            for j in range(i, len(nums)):
                p *= nums[j]
              
                g = gcd(g, nums[j])
                l = (l * nums[j]) // gcd(l, nums[j])
                if p == l * g:
                    ans = max(ans, j - i + 1)
        return ans