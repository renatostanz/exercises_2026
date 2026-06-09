# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import log2
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        search = [root]
        marker = 0
        nodes_to_visit_count = 1
        previous_depth = 0

        x_parent = None
        x_depth = None

        y_parent = None
        y_depth = None

        def bfs(search: list(TreeNode | None), marker: int, nodes_to_visit_count: int) -> None: 
            nonlocal x_parent, x_depth, y_parent, y_depth
            if x_parent is not None and y_parent is not None and x_parent != y_parent and x_depth == y_depth:
                return True
            if nodes_to_visit_count == 0:
                return False

            node = search[marker]
            marker += 1
            if node is not None:
                nodes_to_visit_count -= 1
                if node.left is not None:
                    nodes_to_visit_count += 1
                if node.right is not None:
                    nodes_to_visit_count += 1

                search.append(node.left)
                search.append(node.right)

                if node.val == x:
                    x_depth = int(log2(marker))
                    x_parent = marker // 2

                if node.val == y:
                    y_depth = int(log2(marker))
                    y_parent = marker // 2

            else:
                search.append(None)
                search.append(None)

            return bfs(search, marker, nodes_to_visit_count)

        return bfs(search, marker, nodes_to_visit_count)
