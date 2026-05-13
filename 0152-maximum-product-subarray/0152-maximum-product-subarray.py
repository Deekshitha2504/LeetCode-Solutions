class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxpro=nums[0]
        curmax=1
        curmin=1
        for num in nums:
            if num<0:
                curmax,curmin=curmin,curmax
            curmax=max(num,curmax*num)
            curmin=min(num,curmin*num)
            maxpro=max(curmax,maxpro)
        return maxpro    