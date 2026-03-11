class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur=max_sum=nums[0]
        for i in nums[1:]:
            cur=max(i,cur+i)
            max_sum=max(cur,max_sum)
        
        return max_sum            
