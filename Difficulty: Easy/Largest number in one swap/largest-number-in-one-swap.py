class Solution:
    def largestSwap(self, s):
        lth=len(s)
        mx=-float('inf')
        swap=None
        for ix in range(lth-1,-1,-1):
            ve=int(s[ix])
            if ve>mx:
                rr=ix
                mx=ve
            elif ve<mx:
                swap=(ix,rr,)
        if swap==None:
            return s
        ll,rr=swap
        return s[:ll]+s[rr]+s[ll+1:rr]+s[ll]+s[rr+1:]

