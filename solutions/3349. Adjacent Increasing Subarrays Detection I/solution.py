# Problem: Adjacent Increasing Subarrays Detection I
# Language: python3
# Runtime: 94 ms
# Memory: 18 MB

class Solution:
    def hasIncreasingSubarrays(self, A: List[int], k: int) -> bool:
        B = []
        B = [1]
        count = 1
        ans = 1
        for i in range(1,N:=len(A)):
            if A[i] > A[i-1]:
                count += 1
                
            else:
                count = 1
            B.append(count)
            ans = max(ans, count // 2)
        
        i,j = 0,0
        for i in range(1,N):
            if B[i] < B[i-1]:
                break
        
        i-=1
        j = i+1
        while j < N:
            if j < N-1 and B[j+1] > B[j]:
                while j < N-1 and B[j+1] > B[j]:
                    j += 1
                ans = max(ans, min(B[i],B[j]))
            i = j
            j += 1
        
        return ans >= k