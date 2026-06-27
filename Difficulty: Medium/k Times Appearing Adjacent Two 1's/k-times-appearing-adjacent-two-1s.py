class Solution:
    def helper(self, last, k, l, n):
        if k == 0 and l == n:
            return 1

        if l >= n:
            return 0
            
        if self.dp[last][k][l] != -1:
            return self.dp[last][k][l]

        c = self.helper(0, k, l + 1, n)
        add_one = not (k == 0 and last == 1)
        if add_one:
            c += self.helper(1, k - last, l + 1, n)
        self.dp[last][k][l] = c
        return self.dp[last][k][l]
            
        
    def countStrings(self, n, k): 
        # code here 
        self.dp = [[[-1] * (n + 1) for i in range(k + 1)] for _ in range(2)]
        return self.helper(0, k, 0, n) % (10 ** 9 + 7)