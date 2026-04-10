class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n = len(arr)
        prev_small = [-1]*n
        next_great = [n]*n
        
        stk = []
        for i in range(n):
            while(stk and arr[stk[-1]] >= arr[i]):
                stk.pop()
            if stk:
                prev_small[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n-1, -1, -1):
            while(stk and arr[stk[-1]] <= arr[i]):
                stk.pop()
            if stk:
                next_great[i] = stk[-1]
            stk.append(i)
        
        res = []
        for i in range(n):
            if prev_small[i] != -1 and next_great[i] != n:
                return [arr[prev_small[i]], arr[i], arr[next_great[i]]]
        return res

