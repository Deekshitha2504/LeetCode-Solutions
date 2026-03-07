class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        max_area=0
        while left<right:
            Area=(right-left)*min(height[left],height[right])
            if max_area<Area:
                max_area=Area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area               
