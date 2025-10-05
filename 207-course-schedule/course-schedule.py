from collections import defaultdict, deque 

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """ 

        indegree = [0] * numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        remaining = 0
        while queue:
            course = queue.popleft()
            remaining += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return remaining == numCourses

