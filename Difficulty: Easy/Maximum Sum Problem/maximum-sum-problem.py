class Solution:
    def maxSum(self, n):
        memo = {}

        def solve(x):
            if x == 0:
                return 0

            if x in memo:
                return memo[x]

            # Either keep the number as it is
            # or break it recursively
            memo[x] = max(
                x,
                solve(x // 2) + solve(x // 3) + solve(x // 4)
            )

            return memo[x]

        return solve(n)

