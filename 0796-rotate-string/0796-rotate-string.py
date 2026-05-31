class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # l1=list(s)
        # l2=list(goal)
        # if len(l1)!=len(l2):
        #     return False
        # for x in range(len(l1)):
        #     if l1!=l2:
        #         l1.append(l1.pop(0))
        #     else:
        #         return True
        # return False                    

        if len(s)!=len(goal):
            return False
        return goal in (s+s)     