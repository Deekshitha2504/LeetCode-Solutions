class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # leftSum=[0]
        # rightSum=[]
        # answer=[]
        # summ=sum(nums)
        # lsum=0
        # for num in nums:
        #     lsum+=num
        #     summ-=num
        #     leftSum.append(lsum)
        #     rightSum.append(summ)
        # for i in range(0,len(nums)):
        #     answer.append(abs(leftSum[i]-rightSum[i]))  
        # return answer      

        left_sum = 0
        right_sum = sum(nums)
        answer = []
        
        for num in nums:
            right_sum -= num
            answer.append(abs(left_sum - right_sum))
            left_sum += num
            
        return answer