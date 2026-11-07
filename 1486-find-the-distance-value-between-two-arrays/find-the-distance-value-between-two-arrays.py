class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0

        for i in arr1:
            if all(abs(i - j) > d for j in arr2):
                count += 1

        return count

        