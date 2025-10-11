class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        strings = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    strings[i][j] = 1 + strings[i-1][j-1]
                else:
                    strings[i][j] = max(strings[i-1][j], strings[i][j-1])

        return strings[-1][-1]