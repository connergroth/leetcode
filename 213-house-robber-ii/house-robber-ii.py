class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        def robLinear(nums):
            rob1 = rob2 = 0

            for num in nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(robLinear(nums[1:]), robLinear(nums[:-1]))