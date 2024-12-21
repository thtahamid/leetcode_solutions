class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        # Initialize variables
        visited = set()
        self.components = 0  # Track the number of valid components
        
        def dfs(node):
            # Mark the node as visited
            visited.add(node)
            # Start the subtree sum with the node's value
            subtree_sum = values[node]
            
            for neighbor in tree[node]:
                if neighbor not in visited:
                    # Recursively calculate the subtree sum
                    child_sum = dfs(neighbor)
                    # If the child's sum is divisible by k, it's a valid component
                    if child_sum % k == 0:
                        self.components += 1
                    else:
                        subtree_sum += child_sum
            
            return subtree_sum
        
        # Perform DFS from an arbitrary root (node 0)
        total_sum = dfs(0)
        # If the entire tree's sum is divisible by k, increment components
        if total_sum % k == 0:
            self.components += 1
        
        return self.components