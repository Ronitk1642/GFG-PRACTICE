class Solution:
    def sumDiffPairs(self, arr, k):
        arr.sort()
        total_sum, i = 0, len(arr) - 1
        
        while i > 0:
            if arr[i] - arr[i-1] < k:
                total_sum += arr[i] + arr[i-1]
                i -= 2  # Skip both elements
            else:
                i -= 1  # Skip only the largest element
                
        return total_sum