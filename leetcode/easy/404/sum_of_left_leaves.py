# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum_ = 0
        def search_left_leaves_sum(node: TreeNode|None, is_left: bool) -> None:
            if node is None:
                return None

            if node.left is None and node.right is None and is_left == True:
               self.sum_ += node.val

            search_left_leaves_sum(node.right, False)
            search_left_leaves_sum(node.left, True)

        search_left_leaves_sum(root, False)
        return self.sum_
