class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque([(0, 0)])
        length = 0

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                visited.add((r, c))
                if (r,c) == (rows-1, cols-1):
                    return length + 1

                directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            length += 1

        if (rows-1, cols-1) not in visited:
            return -1

        return length               