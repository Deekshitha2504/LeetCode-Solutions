class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        running_left = 1
        for i in range(n):
            answer[i] = running_left
            running_left *= nums[i]
        
        running_right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= running_right
            running_right *= nums[i]
            
        return answer