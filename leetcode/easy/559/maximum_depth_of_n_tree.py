"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: Node | None) -> int:
        def dfs(node: Node | None, depth: int) -> int:
            if node is None or node.val is None or node.children is None:
                return depth - 1

            children_max_depth = depth
            for i in range(len(node.children)):
                if node.children[i] is None or node.children[i].val is None:
                    continue

                child_max_depth = dfs(node.children[i], depth + 1)
                if children_max_depth < child_max_depth:
                    children_max_depth = child_max_depth

            return children_max_depth

        return dfs(root, 1)
