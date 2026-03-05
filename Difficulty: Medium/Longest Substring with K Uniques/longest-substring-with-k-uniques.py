class Solution:
    def longestKSubstr(self, s, k):
        # code here
        left=0
        n=len(s)
        from collections import defaultdict
        ma=defaultdict(int)
        ans=-1
        for right in range(n):
            ma[s[right]]+=1
            if len(ma)>k:
                while len(ma)>k:
                    
                    ma[s[left]]-=1
                    if ma[s[left]]==0:
                        del ma[s[left]]
                    left+=1
            elif len(ma)==k:
                ans=max(ans,right-left+1)
        return ans