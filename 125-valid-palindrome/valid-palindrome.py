class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        normalized = ''.join([char.lower() for char in s if char.isalnum()])

        left = 0
        right = len(normalized) - 1

        while left < right:
            if not normalized[left] == normalized[right]:
                return False
            left+=1 
            right-=1
        return True
        
                