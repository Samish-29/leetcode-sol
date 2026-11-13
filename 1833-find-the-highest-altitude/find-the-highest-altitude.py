class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        hieghest = 0

        for g in gain:
            altitude += g
            hieghest = max(hieghest, altitude)

        return hieghest