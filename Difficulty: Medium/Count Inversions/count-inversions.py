class Solution:
    def inversionCount(self, arr):
        ret=0
        def quicksort(arr=arr):
            nonlocal ret
            lth=len(arr)
            if lth<=1:
                return
            piv=arr[0]
            left=[]
            right=[]
            for ix in range(1,lth):
                ve=arr[ix]
                if ve<piv:
                    left.append(ve)
                    ret+=len(right)+1
                else:
                    right.append(ve)
            quicksort(left)
            quicksort(right)
        quicksort()
        return ret