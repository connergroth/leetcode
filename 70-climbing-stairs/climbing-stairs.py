class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = two = 1
        
        for n in range(n - 1):
            temp = one 
            one = one + two
            two = temp

        return one 