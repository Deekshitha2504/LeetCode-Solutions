class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts=Counter(nums)
        counts1=sorted(counts.items(), key=lambda items:items[1], reverse=True)
        keyy=[x[0] for x in counts1]
        return keyy[0:k]    
