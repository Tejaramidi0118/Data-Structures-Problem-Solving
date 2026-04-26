# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        self.mode = []
        self.max_count = 0
        self.prev = None
        self.count = 0
        
        self.inorder(root)
        
        return self.mode
    
    def inorder(self, root):
            
            if root is None:
                return
            
            self.inorder(root.left)
            
            if self.prev is None:
                self.prev = root.val
                self.count = 1

            elif self.prev == root.val:
                self.count += 1
                
            else:
                self.prev = root.val
                self.count = 1
            
            if self.count > self.max_count:
                self.max_count = self.count
                self.mode = [root.val]

            elif self.count == self.max_count:
                self.mode.append(root.val)
            
            self.inorder(root.right)