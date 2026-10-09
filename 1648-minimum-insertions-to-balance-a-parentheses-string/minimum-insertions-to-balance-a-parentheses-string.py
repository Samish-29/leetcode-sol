class Solution(object):
    def minInsertions(self, s):
        result = 0
        bracket = 0
        for ch in s:
            if ch == '(':
                bracket += 2
                if bracket % 2 == 1:
                    bracket -= 1
                    result += 1
            
            else:
                bracket -= 1
                if bracket < 0:
                    bracket = 1
                    result += 1
        return result + bracket
                
