# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        preSum = {0:1}

        def dfs(node,curr):
            if not node:
                return 0
            
            curr += node.val

            ans = preSum.get(curr-targetSum,0)

            preSum[curr] = preSum.get(curr,0) + 1

            ans += dfs(node.left,curr)
            ans += dfs(node.right,curr)

            preSum[curr] -= 1
            
            return ans
        
        return dfs(root,0)