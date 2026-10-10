class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        # This was my approach which gave me tle
        #diff = [abs(a - b) for a , b in zip(nums1, nums2)]
        #k = k1 + k2
        #if sum(diff) <= k:
        #    return 0
        #while k > 0:
        #    m = max(diff)
        #    i = diff.index(m)
        #    diff[i] -= 1
        #    k-=1
        #return sum(d * d for d in diff)

        k = k1 + k2

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        # If all differences can be eliminated
        if sum(diff) <= k:
            return 0

        # Frequency array
        max_diff = max(diff)
        freq = [0] * (max_diff + 1)

        for d in diff:
            freq[d] += 1

        # Reduce the largest differences first
        for d in range(max_diff, 0, -1):
            if k == 0:
                break

            # Number of differences to reduce
            moves = min(freq[d], k)

            freq[d] -= moves
            freq[d - 1] += moves
            k -= moves

        # Calculate the sum of squared differences
        ans = 0

        for d in range(len(freq)):
            ans += d * d * freq[d]

        return ans
