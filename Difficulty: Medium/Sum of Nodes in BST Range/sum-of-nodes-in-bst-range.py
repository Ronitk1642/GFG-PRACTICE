class Solution:
    def nodeSum(self, root, l, r):
        self.sum  = 0
        if not root:
            return 0
        if l <= root.data <= r:
            self.sum += root.data
        
        return self.sum + self.nodeSum(root.left, l, r) + self.nodeSum(root.right, l, r)

