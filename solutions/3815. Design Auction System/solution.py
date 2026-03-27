# Problem: Design Auction System
# Language: python3
# Runtime: 388 ms
# Memory: 55.7 MB

from sortedcontainers import SortedList
class AuctionSystem:

    def __init__(self):
        self.A = {}
        self.S = defaultdict(SortedList)
        

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if (userId,itemId) in self.A:
            b = self.A[(userId,itemId)]
            self.S[itemId].remove((b,userId))
        self.A[(userId,itemId)] = bidAmount
        self.S[itemId].add((bidAmount,userId))
        

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        b = self.A[(userId,itemId)]
        del self.A[(userId,itemId)]
        self.S[itemId].remove((b,userId))

    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.S or not self.S[itemId]:
            return -1
        return self.S[itemId][-1][-1]
        


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)