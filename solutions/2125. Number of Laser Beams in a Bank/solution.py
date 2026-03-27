# Problem: Number of Laser Beams in a Bank
# Language: python3
# Runtime: 3 ms
# Memory: 19.5 MB

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        
        A = [x.count('1') for x in bank]
        A = [a for a in A if a > 0]
        if len(A) <= 1: return 0
        b = A[0]
        ans = 0
        for a in A[1:]:
            ans += b * a
            b = a
        return ans