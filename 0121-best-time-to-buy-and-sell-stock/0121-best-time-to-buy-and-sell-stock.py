class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        curlow=prices[0]
        for x in prices:
            curlow=min(curlow,x)
            diff=x-curlow
            maxprof=max(diff,maxprof)
        return maxprof    