# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return []
        
        q = deque([root])
        
        idx = float('inf')
        maxS = float('-inf')
        h = 1
        while q:
            level = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            print(level,sum(level))
            if sum(level) > maxS:
                maxS = sum(level)
                idx = h
            elif sum(level) == maxS:
                maxS = sum(level)
                idx = min(idx,h)

            h += 1

        return idx

# from collections import deque

# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         q = deque([root])
#         maxS = float('-inf')
#         idx = 1
#         h = 1
        
#         while q:
#             size = len(q)
#             level_sum = 0
            
#             for _ in range(size):
#                 node = q.popleft()
#                 level_sum += node.val
                
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
            
#             if level_sum > maxS:
#                 maxS = level_sum
#                 idx = h
            
#             h += 1
        
#         return idx