# Problem: Minimum Operations to Make Array Equal II
# Language: python3
# Runtime: 746 ms
# Memory: 30.4 MB

class Solution:
    def minOperations(self, A: List[int], B: List[int], k: int) -> int:
        if k == 0:
            return 0 if A == B else -1
        N = len(A)
        ans = 0
        i = 0
        l = 0
        r = 0
        while i < N:
            
            if A[i] == B[i]:
                i+=1
                continue
            
            if A[i] < B[i]:
                if B[i] %k  == A[i] % k:
                    l += (B[i] - A[i]) // k
                else:
                    return -1
            else:
                if B[i] %k  == A[i] % k:
                    r += (-B[i] + A[i]) // k
                else:
                    return -1
            
            i += 1
            
        return l if l==r  else -1