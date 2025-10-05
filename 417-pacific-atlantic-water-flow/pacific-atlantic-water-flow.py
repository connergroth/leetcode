from collections import deque

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pac_queue = deque()
        atl_queue = deque()

        rows, cols = len(heights), len(heights[0])

        for r in range(rows):
            pac_queue.append((r, 0))
            atl_queue.append((r, cols - 1))
        for c in range(cols):
            pac_queue.append((0, c))
            atl_queue.append((rows - 1, c))

        pac_visited = set(pac_queue)
        atl_visited = set(atl_queue)

        def bfs(queue, visited):

            while queue:
                r,c = queue.popleft()

                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions: 
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        queue.append((nr,nc))
                        visited.add((nr,nc))

        bfs(pac_queue, pac_visited)
        bfs(atl_queue, atl_visited)
        
        result = list(pac_visited & atl_visited) 
        
        return result