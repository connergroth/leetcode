from collections import defaultdict, deque 

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """ 

        # take prereqs array and construct graph via defaultdict
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        # state tracking [0],[1],[2]
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            elif state[course] == 2:
                return True # already processed

            state[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            state[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

            

                

