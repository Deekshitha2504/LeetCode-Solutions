class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)<=2:
            return sum(cost)
        total=0
        cost.sort(reverse=True)
        for i in range(0,len(cost)):
            if (i+1)%3!=0:        
                total+=cost[i]
        return total        