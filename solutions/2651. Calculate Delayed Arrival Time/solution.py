# Problem: Calculate Delayed Arrival Time
# Language: python3
# Runtime: 32 ms
# Memory: 13.9 MB

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24