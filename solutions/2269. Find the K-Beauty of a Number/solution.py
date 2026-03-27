# Problem: Find the K-Beauty of a Number
# Language: python3
# Runtime: 49 ms
# Memory: 13.7 MB

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        S = str(num)
        return sum( 1 if int(S[i:i+k]) and (num % int(S[i:i+k]) == 0) else 0 for i in range(len(S)-k+1))
            