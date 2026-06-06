# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        paths = self.find_paths(root, [[]])
        return ["->".join(p) for p in paths]


    def find_paths(self, root: Optinal[TreeNode], paths: list[list[str]] = []) -> list[list[str]]:
        paths = [p+[str(root.val)] for p in paths]

        if root.left is None and root.right is None:
            return paths
            
        new_paths = []
        if root.left is not None:
            new_paths = self.find_paths(root.left, paths)
        if root.right is not None:
            new_paths += self.find_paths(root.right, paths)

        return new_paths

