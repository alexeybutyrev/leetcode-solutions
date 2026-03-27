# Problem: Longest Alternating Subarray
# Language: python3
# Runtime: 1279 ms
# Memory: 16.5 MB

class Solution:
    def alternatingSubarray(self, A: List[int]) -> int:
        N = len(A)
        ans = -1
        for i in range(N):
            for j in range(i+1,N):
                B = A[i:j+1]
                x,y = B[0],B[1]
                if y != x+1:
                    continue
                
                count = 2
                for k in range(2,len(B)):
                    if k & 1 and B[k] == y:
                        count += 1
                    elif (k & 1) == 0 and B[k] == x:
                        count += 1
                    else:
                        break
                ans = max(ans,count)
        return ans