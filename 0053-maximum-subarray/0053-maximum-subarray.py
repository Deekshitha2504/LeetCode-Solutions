class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        cur=0
        for num in nums:
            cur=max(num,cur+num)
            maxsum=max(maxsum,cur)
        return maxsum    
            