class Solution(object):
    def sumAndMultiply(self, n):
       s = str(n).replace('0', '')

       if not s:

        return 0
       return int(s) * sum(int(d) for d in s)