# Problem: Design Underground System
# Language: python3
# Runtime: 296 ms
# Memory: 23.9 MB

class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.station_list = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (startStation, t0) = self.customer[id]
        del self.customer[id]
        self.station_list[(startStation,stationName)].append(t-t0)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.station_list[(startStation,endStation)]) / len(self.station_list[(startStation,endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)