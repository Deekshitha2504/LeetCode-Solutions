class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            if i>0 and nums[i-1]==nums[i]:
                continue
            while l<r:
                summ=nums[l]+nums[r]+nums[i]
                if summ==0:
                    res.append([nums[l],nums[r],nums[i]])
                    l+=1
                    while nums[l-1]==nums[l] and l<r:
                        l+=1
                elif summ<0:
                    l+=1
                else:
                    r-=1
        return res                        