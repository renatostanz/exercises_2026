# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, depth: int) -> int:
            if node is None:
                return depth - 1

            if node.left is None:
                return dfs(node.right, depth+1)
            if node.right is None:
                return dfs(node.left, depth+1)

            return min(
                dfs(node.left, depth+1),
                dfs(node.right, depth+1)
            )

        return dfs(root, 1)
