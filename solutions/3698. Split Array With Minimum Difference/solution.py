# Problem: Split Array With Minimum Difference
# Language: python3
# Runtime: 43 ms
# Memory: 29.9 MB

class Solution:
    def splitArray(self, A: List[int]) -> int:
        x = 0
        for y in A:
            if y > x:
                x = y
            else:
                break
        else:
            return abs(sum(A) - A[-1] - A[-1])

        x = inf
        for y in A:
            if y < x:
                x = y
            else:
                break
        else:
            return abs(sum(A) - A[0] - A[0])
        
        

        x = 0
        s1 = 0
        for i,y in enumerate(A):
            if y > x:
                x = y
                mx = y
                s1 += y
            else:
                break

        N = len(A)
        if i < N and A[i] == mx:
            s2 = mx
            i += 1
            x = mx
            for j in range(i,N):
                y = A[j]
                if y >= x: return -1
                s2 += y
                x = y
            return abs(s2-s1)
        x = mx
        s2 = 0
        for j in range(i,len(A)):
            y = A[j]
            s2 += y
            if y >= x: return -1
            x = y
        ans = min(abs(s2 - s1), abs( (s2 + mx) - (s1-mx) ))
        return ans
            