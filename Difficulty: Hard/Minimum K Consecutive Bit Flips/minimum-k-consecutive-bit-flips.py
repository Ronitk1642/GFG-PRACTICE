class Solution:
    def kBitFlips(self, arr, k):
        lth=len(arr)
        status=[0]*(lth+1)
        cur=ans=0
        for ix,ve in enumerate(arr):
            cur^=status[ix]
            if ve^cur==0:
                cur^=1
                if ix+k<=lth:
                    status[ix+k]^=1
                else:
                    return -1
                ans+=1
        return ans