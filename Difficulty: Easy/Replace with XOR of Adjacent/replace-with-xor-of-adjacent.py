class Solution:
    def replaceElements(self, arr):
        # code here
        arr2 = arr.copy()
        
        for idx, val in enumerate(arr):
            if idx == 0:
                arr[idx] = arr2[idx] ^ arr2[idx + 1]
            elif idx == len(arr) - 1:
                arr[idx] = arr2[idx - 1] ^ arr2[idx]
            else:
                arr[idx] = arr2[idx - 1] ^ arr2[idx + 1]
        
        return arr2