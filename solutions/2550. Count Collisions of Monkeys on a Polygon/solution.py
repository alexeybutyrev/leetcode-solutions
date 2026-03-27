# Problem: Count Collisions of Monkeys on a Polygon
# Language: python3
# Runtime: 38 ms
# Memory: 13.8 MB

import math
class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        return (pow(2,n,MOD) - 2) % MOD