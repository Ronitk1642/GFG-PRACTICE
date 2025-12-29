class Solution:
    def kthElement(self, a, b, k):
        # code here
        newarr=sorted(a+b)
        return newarr[k-1]