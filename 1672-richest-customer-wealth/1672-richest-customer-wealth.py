class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # return max(sum(lambda x:for x in accounts))
        # maxsum=0
        # for x in accounts:
        #     maxsum=max(maxsum,sum(x))
        # return maxsum    
        return max(sum(x) for x in accounts)