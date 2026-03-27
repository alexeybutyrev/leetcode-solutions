# Problem: Angle Between Hands of a Clock
# Language: python3
# Runtime: 48 ms
# Memory: 13.7 MB

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hours = minutes / 60 * 5 if hour == 12 else hour * 5  + (minutes / 60) * 5
        if hours == 12 and minutes == 0:
            return 0
        return min(360 - abs(minutes - hours) * 6, abs(minutes - hours) * 6)