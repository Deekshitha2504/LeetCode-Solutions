# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: return []
        res=[]
        que=deque([root])
        while que:    
            path=[]
            size=len(que)
            for x in range(size):
                node=que.popleft()
                path.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            res.append(path)
        return res[::-1]    

            

