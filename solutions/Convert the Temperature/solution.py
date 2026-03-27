# Problem: Convert the Temperature
# Language: python3
# Runtime: 40 ms
# Memory: 13.8 MB

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15 , celsius * 1.80 + 32.00]