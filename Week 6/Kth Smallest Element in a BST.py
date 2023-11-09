# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        self.k = k

        def dfs(root):
            if root is None:
                return
            
            dfs(root.left)
            self.k -= 1
            if self.k >= 0:
                self.ans = root.val
            dfs(root.right)

        dfs(root) 
        return self.ans
        
