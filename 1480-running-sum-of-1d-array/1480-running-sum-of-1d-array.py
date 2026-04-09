class Solution(object):
    
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        res=[]
        for i in nums:
            sum+=i
            res.append(sum)
        return res    