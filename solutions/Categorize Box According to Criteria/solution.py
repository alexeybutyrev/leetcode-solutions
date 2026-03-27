# Problem: Categorize Box According to Criteria
# Language: python3
# Runtime: 27 ms
# Memory: 13.9 MB

class Solution:
    def categorizeBox(self, l: int, w: int, h: int, m: int) -> str:
        V = l * w * h
        if (V >= 10**9 or l >= 10**4 or w >= 10**4 or h >= 10**4) and m >= 100:
            return "Both"
        elif (V >= 10**9 or l >= 10**4 or w >= 10**4 or h >= 10**4):
            return "Bulky"
        elif m >= 100:
            return "Heavy"
        return "Neither"