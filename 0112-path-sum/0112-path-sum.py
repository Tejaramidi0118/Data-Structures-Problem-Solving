# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,s):
            if root==None:
                return False

            s += root.val

            if not root.left and not root.right:
                return s == targetSum

            
            return dfs(root.left,s) or dfs(root.right,s)



        return dfs(root,0)

            
