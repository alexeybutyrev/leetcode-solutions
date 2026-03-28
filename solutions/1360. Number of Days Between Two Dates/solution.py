# Problem: Number of Days Between Two Dates
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = date1.split("-")
        y2, m2, d2 = date2.split("-")
        d1 = datetime(int(y1), int(m1), int(d1))
        d2 = datetime(int(y2), int(m2), int(d2))
        return abs((d2 - d1).days)
        
        