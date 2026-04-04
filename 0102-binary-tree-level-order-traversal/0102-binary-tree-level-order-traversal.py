# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: return []
        result=[]
        que=deque([root])
        while que:
            length=len(que)
            curlvl=[]
            for x in range(length):
                node=que.popleft()
                curlvl.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            result.append(curlvl)
        return result        