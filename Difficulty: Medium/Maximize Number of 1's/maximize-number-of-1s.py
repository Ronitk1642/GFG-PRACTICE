class Solution:
    def maxOnes(self, arr, k):
        l = 0
        zero_count = 0
        max_len = 0

        for r in range(len(arr)):
            if arr[r] == 0:
                zero_count += 1

            # If more than k zeros, shrink window
            while zero_count > k:
                if arr[l] == 0:
                    zero_count -= 1
                l += 1

            # Update maximum length
            max_len = max(max_len, r - l + 1)

        return max_len