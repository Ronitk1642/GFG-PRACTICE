class Solution:
    def countDistinct(self, arr, k):
                # Code here
        from collections import Counter
        
        window = Counter(arr[:k])
        ans = [len(window)]
        for i in range(k, len(arr)):
            out_elem = arr[i - k]
            in_elem = arr[i]
            window[out_elem] -= 1
            if window[out_elem] == 0:
                del window[out_elem]
            window[in_elem] += 1
            ans.append(len(window))
        return ans