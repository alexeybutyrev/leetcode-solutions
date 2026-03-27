# Problem: Furthest Point From Origin
# Language: python3
# Runtime: 46 ms
# Memory: 16.4 MB

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        S = moves
        S1 = S.replace('_', 'L')
        S2 = S.replace('_', 'R')
        
        def check(s):
            ans = 0
            for x in s:
                if x == 'L':
                    ans -= 1
                else:
                    ans += 1
            return ans
        
        return max(abs(check(S1)),abs(check(S2)))
            