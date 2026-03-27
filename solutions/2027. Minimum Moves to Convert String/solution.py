# Problem: Minimum Moves to Convert String
# Language: python3
# Runtime: 32 ms
# Memory: 14.1 MB

class Solution:
    def minimumMoves(self, s: str) -> int:
        k = 0
        count = 0
        for i in range(len(s)):
            if s[i] == 'X':
                if k == 0:
                    count += 1
                    k+=1
                else:
                    k += 1
                    if k == 3:
                        k = 0
            else:
                if k:
                    k += 1
                    if k == 3:
                        k = 0
        
        return count