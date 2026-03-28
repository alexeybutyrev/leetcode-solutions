# Problem: Next Greater Element III
# Language: python3
# Runtime: 24 ms
# Memory: 14.3 MB

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        A = list(str(n))
        N = len(A)
        if 1 == N:
            return -1
        
        # find i
        for i in range(N-2, -1, -1):
            if A[i] < A[i+1]:
                break
        
        if i == 0 and A[i] > A[i+1]:
            return -1
        
        for j in range(i+1, N):
            if A[j] <= A[i]:
                break
        if A[i] >= A[j]:
            j -= 1
        #if j - 1 > i:
        #    j = j - 1
        #print(i,j)
        
        A[j], A[i] = A[i], A[j]
        #print(A)
        
        
        v = int("".join(A[:i+1] + list(reversed(A[i+1:]))))
        #print(v,n)
        return v if not(v >> 32 - 1) and v > n else -1
    