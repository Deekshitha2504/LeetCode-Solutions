class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # res=[]
        # for n1 in nums1:
        #     if n1 in nums2:
        #         res.append(n1)
        #         nums2.remove(n1)
        # return res 
        nums1.sort()
        nums2.sort()
        i,j=0,0
        res=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1         
        return res                