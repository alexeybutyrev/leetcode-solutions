# Problem: Pairs of Songs With Total Durations Divisible by 60
# Language: python3
# Runtime: 220 ms
# Memory: 17.6 MB

from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        
        count = 0
        for t in time:
            c = t%60
            if c == 0:
                count += d[0]
            else:
                count += d[60 - c]
            d[c] += 1
        return count