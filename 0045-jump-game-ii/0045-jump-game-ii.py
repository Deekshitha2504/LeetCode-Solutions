class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
            
        count = 0
        farthest = 0
        current_end = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                count += 1             
                current_end = farthest  
                
        return count