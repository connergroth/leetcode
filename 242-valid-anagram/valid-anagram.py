class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        seen = {}
        for i, char in enumerate(s):
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1

        for char in t:
            if char in seen and seen[char] > 0:
                seen[char] -= 1
            else:
                return False

        return True