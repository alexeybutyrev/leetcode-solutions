# Problem: Zero Array Transformation II
# Language: python3
# Runtime: 1062 ms
# Memory: 57.2 MB

class Solution:
    def minZeroArray(self, A: List[int], Q: List[List[int]]) -> bool:
        if sum(A) == 0: return 0
        N = len(A)
        BIT = [0] * (N + 1)
        
        # update BIT for prefix increments ( arr[i] += val for i from 1 to idx)
        def update(i, val):
            while i:
                BIT[i] += val 
                i -= i & (-i)
        
        def getValue(i):
            s = 0
            while i < N + 1:
                s += BIT[i]
                i += i & (-i)
            return s
        
        k = 0
        ind = 1
        for a,b,x in Q:
            k += 1
            update(a, -x)
            update(b + 1, x)
            
            while ind <= N:
                if getValue(ind) < A[ind - 1]:
                    break
                ind += 1
                
            if ind == N + 1:
                return k
        return -1