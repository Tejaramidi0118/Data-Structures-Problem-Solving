# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        count = 0
        q = [(root, root.val)]

        while q:
            node, max_so_far = q.pop()

            if node.val >= max_so_far:
                count += 1

            new_max = max(max_so_far, node.val)

            if node.left:
                q.append((node.left, new_max))
            if node.right:
                q.append((node.right, new_max))

        return count
