class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)

        # Square all elements
        arr = [x*x for x in arr]

        # Put all squares in a set
        s = set(arr)

        # Check pairs
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] in s:
                    return True

        return False