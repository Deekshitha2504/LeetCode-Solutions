# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxsum=float('-inf')
        def getsum(node):
            if not node:return 0
            left=max(getsum(node.left),0)
            right=max(getsum(node.right),0)
            cursum=node.val+left+right
            self.maxsum=max(cursum,self.maxsum)
            return node.val+max(left,right)
        getsum(root)
        return self.maxsum    