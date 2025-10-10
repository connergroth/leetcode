from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh = 0
        minutes = 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        if not grid:
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        if fresh == 0:
            return 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2

                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            minutes += 1

        if fresh > 0:
            return -1

        return minutes