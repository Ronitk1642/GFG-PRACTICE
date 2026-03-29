class Solution:
    def countPartitions(self, arr, diff):
        # code here
        '''
            total 
            s1 + s2 = total
            s1 - s2 = diff
            
            2s1 = total + diff
            s1 = (total + diff) // 2
        
        
        
        '''
        def f(ind, target):
            
            if target == 0:
                return 1
            if ind >= len(arr):
                if target == 0:
                    return 1
                return 0
            if (ind, target) in dp:
                return dp[(ind, target)]
            p1, p2 = 0, 0
            p1 = f(ind + 1, target - arr[ind])
            p2 = f(ind + 1, target)
            dp[(ind, target)] = p1 + p2
            return p1 + p2
            
        n = len(arr)
        
        v = (sum(arr) + diff)
        if v&1:
            return 0
        s = v//2
        arr.sort()
        dp = {}
        return f(0, s)