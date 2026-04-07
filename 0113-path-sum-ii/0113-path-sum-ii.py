# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res=[]
        def dfs(node, cur_sum, path):
            if not node:
                return
            path.append(node.val)    
            if not node.left and not node.right and cur_sum==node.val:
                res.append(list(path))
            dfs(node.left, cur_sum-node.val, path)        
            dfs(node.right, cur_sum-node.val, path)
            path.pop()
        dfs(root, targetSum, [])
        return res    