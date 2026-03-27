# Problem: Minimum Pair Removal to Sort Array I
# Language: python3
# Runtime: 19 ms
# Memory: 19.5 MB

class Solution:
    def minimumPairRemoval(self, A: List[int]) -> int:
        def check(A):
            if len(A) == 1: return True
            return all(A[i+1] >= A[i] for i in range(len(A)-1))
        
        ans = 0
        while True:
            if check(A): return ans
            s = inf
            for i in range(len(A)-1):
                s = min(A[i+1] + A[i],s)
            B = []

            for i,x in enumerate(A):
                if B and B[-1] + x == s:
                    B.append(B.pop() + x)
                    break
                else:
                    B.append(x)
            for j in range(i+1, len(A)):
                B.append(A[j])
            A = B[:]
            ans += 1
        return ans
