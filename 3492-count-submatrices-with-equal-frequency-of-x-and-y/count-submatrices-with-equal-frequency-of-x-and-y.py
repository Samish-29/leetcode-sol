class Solution(object):
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        prefix_sum = [[0]*n for _ in range(m)]
        prefix_x = [[0]*n for _ in range(m)]
        
        def get(ps, i, j):
            if i < 0 or j < 0:
                return 0
            return ps[i][j]
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                prefix_sum[i][j] = (
                    val
                    + get(prefix_sum, i-1, j)
                    + get(prefix_sum, i, j-1)
                    - get(prefix_sum, i-1, j-1)
                )
                is_x = 1 if grid[i][j] == 'X' else 0
                prefix_x[i][j] = (
                    is_x
                    + get(prefix_x, i-1, j)
                    + get(prefix_x, i, j-1)
                    - get(prefix_x, i-1, j-1)
                )
                if prefix_sum[i][j] == 0 and prefix_x[i][j] > 0:
                    count += 1
        
        return count
        