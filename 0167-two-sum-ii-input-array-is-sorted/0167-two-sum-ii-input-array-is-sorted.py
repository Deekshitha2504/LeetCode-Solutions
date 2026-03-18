class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for j in range(len(numbers)):
            num=numbers[j]
            if num not in hashmap:
                hashmap[num]=j
            else:
                hashmap[num]+=1

        for j in range(len(numbers)):
            num=numbers[j] 
            cur=target-num
            if cur in hashmap:
                l=[j+1,hashmap[cur]+1]
                return l
        return [0]
