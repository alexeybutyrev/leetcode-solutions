# Problem: Shortest Impossible Sequence of Rolls
# Language: python3
# Runtime: 1859 ms
# Memory: 31.4 MB

from sortedcontainers import SortedList
class Solution:
    def shortestSequence(self, A: List[int], k: int) -> int:
        c = Counter()
        ans = 1
        for a in A:
            c[a] += 1
            if len(c) == k:
                c = Counter()
                ans += 1
        return ans