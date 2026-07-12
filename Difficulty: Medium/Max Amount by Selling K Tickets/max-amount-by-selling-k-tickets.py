class Solution:
    def maxAmount(self, arr, k):
        from heapq import heapify, heappop
        MODULO = 10**9 + 7
        h = [-a for a in arr]
        heapify(h)
        curr_price, sellers_count, earned = -h[0], 0, 0
        while k and curr_price:
            while h and curr_price == -h[0]:
                heappop(h)
                sellers_count += 1
            next_price = -h[0] if h else 0
            steps = curr_price - next_price
            q, r = divmod(k, sellers_count)
            if q < steps:
                steps = q
                next_price = curr_price - q
                earned = (earned + next_price * r) % MODULO
                k -= r
            # An amout each of the "sellers_count" will earn
            # until the "next_price" when a new seller appears
            gain = (curr_price + next_price + 1) * steps // 2
            earned = (earned + gain * sellers_count) % MODULO
            k -= steps * sellers_count
            curr_price = next_price
        return earned