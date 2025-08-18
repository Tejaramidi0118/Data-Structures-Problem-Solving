# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        if not root:
            return True
        
        q = [root]

        while q:
            temp = q.pop(0)

            l = height(temp.left)
            r = height(temp.right)

            if abs(l - r) > 1:
                return False

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        return True
