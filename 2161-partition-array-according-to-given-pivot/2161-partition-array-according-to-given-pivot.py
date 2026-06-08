class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        answer=[pivot]*len(nums)
        i,j=0,len(nums)-1
        r,l=0,len(answer)-1
        while i<len(nums) and j>=0:
            if nums[i]<pivot:
                answer[r]=nums[i]
                r+=1
            if nums[j]>pivot:
                answer[l]=nums[j]
                l-=1
            j-=1        
            i+=1 
        return answer       
