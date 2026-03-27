# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        

        if not root: return None #if no tree
        root.left,root.right=root.right,root.left #swap the nodes along with sub nodes if there
        self.invertTree(root.left) #do same taking left child
        self.invertTree(root.right) #do same taking right child

        return root #return tree👌