"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # If the root is None, return an empty list
        if not root:
            return []

        res = []

        # Define the DFS function
        def dfs(root):
            # Recursively call dfs for each child of the current node
            for x in root.children:
                dfs(x)
            # Append the value of the current node to the result list
            res.append(root.val)

        # Start DFS from the root
        dfs(root)

        # Return the result list containing node values in post-order
        return res
        