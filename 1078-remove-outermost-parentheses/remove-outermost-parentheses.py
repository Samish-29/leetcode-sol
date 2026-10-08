class Solution(object):
    def removeOuterParentheses(self, s):
        result = ""
        bracket = 0 
        for ch in s:
            if ch == '(':
                if bracket > 0:
                    result += ch
                bracket += 1
            else:
                bracket -= 1
                if bracket > 0:
                    result += ch
        return result