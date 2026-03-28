# Problem: Design Parking System
# Language: python3
# Runtime: 140 ms
# Memory: 14.6 MB

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.space[carType-1] > 0:
            self.space[carType-1] -=1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)