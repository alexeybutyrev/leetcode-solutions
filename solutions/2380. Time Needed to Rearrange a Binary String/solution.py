# Problem: Time Needed to Rearrange a Binary String
# Language: python3
# Runtime: 151 ms
# Memory: 13.8 MB

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0
        while "01" in s:
            s = s.replace("01","10")
            count += 1
        return count