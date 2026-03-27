# Problem: Minimum Suffix Flips
# Language: python3
# Runtime: 560 ms
# Memory: 14.3 MB

class Solution:
    def minFlips(self, target: str) -> int:
        target = target.lstrip("0")
        count = 0
        while target:
            target = target.rstrip(target[-1])
            count+=1
        return count
        