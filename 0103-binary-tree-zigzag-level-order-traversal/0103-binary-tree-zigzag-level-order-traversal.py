# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: return[]
        result=[]
        que=deque([root])
        lvl=False
        while que:
            size=len(que)
            curlvl=[]
            for x in range(size):
                node=que.popleft()
                curlvl.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            if lvl:
                result.append(curlvl[::-1]) 
            else:      
                result.append(curlvl)
            lvl= not lvl    
        return result            