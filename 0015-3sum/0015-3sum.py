class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol=[]# the final list
        nums.sort()#sorting to find the triplets easily
        for i in range(len(nums)):# taking i as ref
            if i>0 and nums[i]==nums[i-1]:#to skip duplicates
                continue
            j,k=i+1,len(nums)-1 #adding two other pointers for b&c of the triplet
            while j<k:#so that we dont keep going through the same numbers
                summ=nums[i]+nums[j]+nums[k]# calculating the sum
                if summ==0:# append the combi if the sum==0
                    sol.append([nums[i],nums[j],nums[k]])
                    j+=1#incrementing j to find different combi
                    while nums[j]==nums[j-1] and j<k:# to skip duplicates
                        j+=1
                elif summ<0:#if sum is lower than 0 then increment j for larger sum
                    j+=1    
                else:#if sum is larger than 0 then decrement k for lower sum
                    k-=1    
        return sol            