class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {} # num : count

        for i, n in enumerate(nums):
            seen[n] = seen.get(n, 0) + 1 
            if seen.get(n) >=2:
                return True
        return False
