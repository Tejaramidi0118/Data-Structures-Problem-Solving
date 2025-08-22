# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        output = []
        q = deque([(root, root.val, [root.val])])
        
        while q:
            node, val, path = q.popleft()

            if not node.left and not node.right and val == targetSum:
                output.append(path)

            if node.left:
                q.append((node.left, val + node.left.val, path + [node.left.val]))
            
            if node.right:
                q.append((node.right, val + node.right.val, path + [node.right.val]))

        return output
