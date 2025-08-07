class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        pairs = list(count.items())      
        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        top_k_pairs = sorted_pairs[:k]
        
        result = []
        for pair in top_k_pairs:
            result.append(pair[0])
        return result