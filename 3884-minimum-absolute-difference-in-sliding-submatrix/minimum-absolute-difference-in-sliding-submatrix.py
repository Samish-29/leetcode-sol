class Solution(object):
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                elements = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        elements.append(grid[x][y])
                elements.sort()
                min_diff = float('inf')
                for p in range(1, len(elements)):
                    if elements[p] != elements[p - 1]:
                        min_diff = min(min_diff, elements[p] - elements[p - 1])
                ans[i][j] = 0 if min_diff == float('inf') else min_diff

        return ans