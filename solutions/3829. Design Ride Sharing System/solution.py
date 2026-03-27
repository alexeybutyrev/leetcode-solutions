# Problem: Design Ride Sharing System
# Language: python3
# Runtime: 112 ms
# Memory: 20.4 MB

from sortedcontainers import SortedList
class RideSharingSystem:

    def __init__(self):
        self.t = 0
        self.RT = SortedList()
        self.DT = SortedList()
        self.R = {}
        self.D = {}
        self.RR = {}
        self.RD = {}
        

    def addRider(self, riderId: int) -> None:
        self.t += 1
        self.RT.add(self.t)
        self.R[self.t] = riderId
        self.RR[riderId] = self.t

    def addDriver(self, driverId: int) -> None:
        self.t += 1
        self.DT.add(self.t)
        self.D[self.t] = driverId
        self.RD[driverId] = self.t

    def matchDriverWithRider(self) -> List[int]:
        if not self.DT or not self.RT: return [-1,-1]
        tr = self.RT.pop(0)
        td = self.DT.pop(0)

        rid, dir = self.R[tr], self.D[td]
        
        
        del self.RR[rid]
        del self.RD[dir]
        return [dir,rid]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.RR:
            tr = self.RR[riderId]
            self.RT.remove(tr)
            del self.RR[riderId]


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)