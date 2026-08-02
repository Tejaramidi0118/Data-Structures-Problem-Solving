# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root,1)])

        while q:
            curr, dep = q.popleft()

            if not curr.left and not curr.right:
                return dep
            
            if curr.left:
                q.append((curr.left,dep+1))
            
            if curr.right:
                q.append((curr.right,dep+1))
        
