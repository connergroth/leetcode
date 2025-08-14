class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for num in nums:
            seen.add(num)
        
        max_length = 0
        for s in seen:
            length = 1
            if s - 1 not in seen:
                while s + 1 in seen:
                    length+=1
                    s+=1
                if length > max_length:
                    max_length = length

        return max_length