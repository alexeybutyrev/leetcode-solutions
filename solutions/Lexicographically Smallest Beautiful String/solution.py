# Problem: Lexicographically Smallest Beautiful String
# Language: python3
# Runtime: 612 ms
# Memory: 19.1 MB

class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        A = [ord(l) - ord('a') for l in s]
        
        N = len(A)
        i = N - 1
        pr = False
        A[i] += 1
        while i >= 0:
            if A[i] == k:
                i -=1
            elif A[i] not in A[max(i-2,0):i]:
                break
            A[i] += 1
        
        if i < 0: return ''
        
        
        for j in range(i+1,N):
            A[j] = min({0, 1, 2} - set(A[max(0, j - 2): j]))
        
        return ''.join(chr(ord('a') + x) for x in A)