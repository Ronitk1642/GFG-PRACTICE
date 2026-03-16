'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
       def countAllPaths(self, root, k):
        prefix_sums = {0: 1}
        
        def dfs(node: Node, curr_sum: int) -> int:
            if node is None:
                return 0
            curr_sum += node.data
            count = prefix_sums.get(curr_sum - k, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            left_count = dfs(node.left, curr_sum)
            right_count = dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1
            return count + left_count + right_count
        
        return dfs(root, 0)