class Solution:
    def validGroups(self, s: str) -> int:
        n = len(s)
        
        # Max possible digit sum for a string of length 100 is 100 * 9 = 900
        # memo[idx][prev_sum] stores the number of valid ways
        memo = [[-1] * 901 for _ in range(n)]
        
        def solve(idx: int, prev_sum: int) -> int:
            # Base Case: Reached the end of the string successfully
            if idx == n:
                return 1
                
            # Return cached result if already calculated
            if memo[idx][prev_sum] != -1:
                return memo[idx][prev_sum]
                
            current_sum = 0
            ways = 0
            
            # Form all possible contiguous sub-groups starting from 'idx'
            for i in range(idx, n):
                current_sum += int(s[i])
                
                # Condition: Current sub-group sum must be non-decreasing (>= prev_sum)
                if current_sum >= prev_sum:
                    ways += solve(i + 1, current_sum)
                    
            memo[idx][prev_sum] = ways
            return ways

        # Start recursion from index 0 with an initial previous sum of 0
        return solve(0, 0)