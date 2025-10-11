class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ways = [[0] * n for _ in range(m)]

        for r in range(m):
            ways[r][0] = 1

        for c in range(n):
            ways[0][c] = 1

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    ways[r][c] = 1  
                else:
                    ways[r][c] = ways[r-1][c] + ways[r][c-1]
        
        return ways[m - 1][n - 1]