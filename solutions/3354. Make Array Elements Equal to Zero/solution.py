# Problem: Make Array Elements Equal to Zero
# Language: python3
# Runtime: 38 ms
# Memory: 16.8 MB

class Solution:
    def countValidSelections(self, A: List[int]) -> int:
        before = 0
        ans = 0
        for i in range(N:=len(A)):
            
            if A[i] == 0:
                after = 0
                for x in range(i+1,N):
                    after += A[x]
                if before == after:
                    ans += 2
                if before == after + 1:
                    ans += 1
                if before == after - 1:
                    ans += 1
            before += A[i]
        return ans