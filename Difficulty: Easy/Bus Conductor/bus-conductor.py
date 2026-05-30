class Solution:
    def findMoves(self, chairs, passengers):
        chairs.sort()
        passengers.sort()
        moves = 0 
        for ch, ps in zip(chairs, passengers):
            moves += abs(ch-ps)
        return moves