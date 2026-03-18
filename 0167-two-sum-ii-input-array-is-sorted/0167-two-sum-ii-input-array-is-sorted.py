class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap={}
        # for j in range(len(numbers)):
        #     num=numbers[j]
        #     if num not in hashmap:
        #         hashmap[num]=j
        #     else:
        #         hashmap[num]+=1

        # for j in range(len(numbers)):
        #     num=numbers[j] 
        #     cur=target-num
        #     if cur in hashmap:
        #         l=[j+1,hashmap[cur]+1]
        #         return l
        # return [0]
        left=0
        right=len(numbers)-1
        while left<right:
            num1=numbers[left]
            num2=numbers[right]
            if num1+num2==target:
                return [left+1, right+1]
            elif num1+num2>target:
                right-=1
            else:
                left+=1
        return [0]                

