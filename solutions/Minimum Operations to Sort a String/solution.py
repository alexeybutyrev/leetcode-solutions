# Problem: Minimum Operations to Sort a String
# Language: python3
# Runtime: 535 ms
# Memory: 23.4 MB

class Solution:
    def minOperations(self, S: str) -> int:
        if len(S) == 2 and S[0] > S[1]: return -1
        ANS = sorted(list(S))
        if list(S) == ANS: return 0

        
        S2 = [S[0]] + sorted(list(S)[1:])
        if ANS == S2:
            return 1

        S1 = sorted(list(S)[:-1]) + [S[-1]]
        if ANS == S1:
            return 1

        if ANS == [S1[0]] + sorted(S1[1:]):
            return 2

        if ANS == sorted(S2[:-1]) + [S2[-1]]:
            return 2
        return 3
        
        
        
        