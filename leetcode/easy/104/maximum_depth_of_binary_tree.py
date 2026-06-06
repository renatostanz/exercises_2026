# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_max_depth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if root is None:
            return depth

        left_depth = self.find_max_depth(root.left, depth+1)
        right_depth = self.find_max_depth(root.right, depth+1)

        if left_depth >= right_depth:
            return left_depth
        return right_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.find_max_depth(root, 0)
