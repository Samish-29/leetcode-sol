class Solution(object):
    def maxSumOfSquares(self, num, sums):
        if sums > 9 * num:
            return ""

        ans = []

        while sums >= 9:
            ans.append('9')
            sums-= 9

        if sums > 0:
            ans.append(str(sums))

        ans.extend(['0'] * (num - len(ans)))

        return ''.join(ans)



        