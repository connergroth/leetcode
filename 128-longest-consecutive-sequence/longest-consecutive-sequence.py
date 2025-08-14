class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for num in nums:
            seen.add(num)

        if not seen:
            return 0
        
        length = 1
        max_length = 1
        for s in seen:
            if s - 1 not in seen:
                while s + 1 in seen:
                    length+=1
                    if length > max_length:
                        max_length = length
                    s+=1
                length = 1
   
        return max_length