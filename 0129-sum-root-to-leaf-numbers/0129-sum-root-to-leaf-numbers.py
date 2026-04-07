# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.Summ=0
        def dfs(node,sumstr):
            if not node: return
            sumstr+=str(node.val)
            if not node.left and not node.right:
                self.Summ+=int(sumstr)
            dfs(node.left,sumstr)            
            dfs(node.right,sumstr)
        dfs(root,"")    
        return self.Summ    