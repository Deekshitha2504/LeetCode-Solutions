class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # for x in range(len(matrix)):
        #     if matrix[x][0]<=target:
        #         for y in range(len(matrix[0])):
        #             if matrix[x][y]==target:
        #                 return True
        # return False    
        row, col=len(matrix), len(matrix[0])
        low, high=0, (row*col)-1
        while low<=high:
            mid=(low+high)//2            
            midval=matrix[mid//col][mid%col]
            if midval==target:
                return True
            elif midval>target:
                high=mid-1
            else:
                low=mid+1
        return False                