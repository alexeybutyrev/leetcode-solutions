# Problem: Minimum Moves to Reach Target Score
# Language: python3
# Runtime: 55 ms
# Memory: 14.3 MB

class Solution:
    def minMoves(self, T: int, mD: int) -> int:
        ans = 0
        while T > 1:
            if not mD:
                ans += T - 1
                break
            if T % 2 == 1:
                ans += 1
                T -= 1
            else:
                T //= 2
                mD -= 1
                ans += 1
                
        return ans
        