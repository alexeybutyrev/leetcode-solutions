# Problem: Numbers At Most N Given Digit Set
# Language: python3
# Runtime: 40 ms
# Memory: 14.2 MB

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        N = str(n)
        n = len(N)
        ND = len(digits)
        ans = sum(ND ** i for i in range(1,n))
        i = 0
        while i < len(N):
            ans += sum(c < N[i] for c in digits) * (ND ** (n-i-1))
            if N[i] not in digits: break
            i+=1
        return ans + (i==n)
    