class Solution:

    def maxCircularSum(self, arr):

        # code here

        ts=sum(arr)

        mas=float('-inf')

        cs=0

        for i in arr:

            cs+=i

            mas=max(mas,cs)

            cs=max(cs,0)

        mis=float('inf')

        cs=0

        for i in arr:

            cs+=i

            mis=min(mis,cs)

            cs=min(0,cs)

        mac=ts-mis

        return mas if not mac else max(mas,mac)

