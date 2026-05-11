class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapp={}
        for i,num in enumerate(nums):
            if num in mapp and abs(mapp[num]-i)<=k:
                return True 
            mapp[num]=i    
        return False                