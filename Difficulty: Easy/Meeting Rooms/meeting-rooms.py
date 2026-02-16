class Solution:
    def canAttend(self, arr):
        # Code Here
        arr.sort(key=lambda x:(x[1],x[0],))
        prv=-float('inf')
        for sta,sto in arr:
            if prv>sta:
                return False
            prv=sto
        return True 
        