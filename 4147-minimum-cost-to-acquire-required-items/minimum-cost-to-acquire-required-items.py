class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        option1 = need1 * cost1 + need2 * cost2

        option2 = max(need1, need2) * costBoth
        option3 = (min(need1, need2) * costBoth +
                   (need1 - min(need1, need2)) * cost1 +
                   (need2 - min(need1, need2)) * cost2)


       

        return min(option1, option2, option3)

       