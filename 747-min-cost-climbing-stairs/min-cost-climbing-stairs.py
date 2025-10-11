class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """       
        two = cost[0]
        one = cost[1]
        
        for i in range(2, len(cost)):
            temp = one
            one = cost[i] + min(one, two)
            two = temp

        return min(one, two)
