class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # s=0
        # f=1
        # while f<len(nums):
        #     if nums[s]==0:
        #         if nums[f]==0:
        #             f+=1
        #         else:    
        #             nums[s],nums[f]=nums[f],nums[s]
        #             s+=1
        s=0
        for f in range(len(nums)):
            if nums[f]!=0:
                nums[s],nums[f]=nums[f],nums[s]
                s+=1
                