class Solution:
    def minimumCost(self, cost, w):
        INF = float('inf')

        dp = [INF] * (w + 1)
        dp[0] = 0

        n = len(cost)

        for j in range(n):
            if cost[j] == -1:
                continue

            wt = j + 1

            for i in range(wt, w + 1):
                dp[i] = min(dp[i], dp[i - wt] + cost[j])

        return dp[w] if dp[w] != INF else -1

