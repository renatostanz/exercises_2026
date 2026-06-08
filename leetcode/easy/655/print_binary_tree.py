# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
from math import log2

class Solution:
    def printTree(self, root: TreeNode| None) -> list[list[str]]:
        tree = []
        nodes_count = 1
        search = [root]
        def bfs() -> None:
            nonlocal nodes_count
            if nodes_count == 0:
                return None

            node = search.pop(0)
            if node is None:
                tree.append("")
                search.append(None)
                search.append(None)
            else:
                tree.append(str(node.val))
                nodes_count -= 1
                search.append(node.left)
                search.append(node.right)

                if node.left is not None:
                    nodes_count += 1
                if node.right is not None:
                    nodes_count += 1

            return bfs()


        def fill_tree() -> None: 
            lower_bound = int(log2(len(tree)))
            missing_null_values = 2*2**lower_bound - len(tree) - 1

            print(missing_null_values, len(tree))
            for i in range(missing_null_values):
                tree.append("")

        bfs()
        fill_tree()

        offset = 0
        current_spacing = 1
        level_init_marker = (len(tree) // 2) 
        level_end_marker = len(tree) - 1

        output_tree = []
        while level_end_marker >= level_init_marker:
            level = []

            for i in range(offset):
                level.append("")

            tree_piece = tree[level_init_marker:level_end_marker]
            for i in tree_piece:
                level.append(i)
                for u in range(current_spacing):
                    level.append("")

            level.append(tree[level_end_marker])

            for i in range(offset):
                level.append("")

            output_tree.append(level)
            current_spacing = current_spacing * 2 + 1

            if offset == 0:
                offset = 1 
            else:
                offset = current_spacing // 2

            level_end_marker = level_init_marker - 1
            level_init_marker //= 2

        return output_tree[::-1]
