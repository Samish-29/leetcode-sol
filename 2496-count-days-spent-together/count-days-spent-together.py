class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        a = max(arriveAlice, arriveBob)
        b = min(leaveAlice, leaveBob)

        if a > b:
            return 0

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def convert(date):
            m, d = map(int, date.split('-'))
            return sum(days[:m-1]) + d

        return convert(b) - convert(a) + 1
       