# Problem: The Latest Time to Catch a Bus
# Language: python3
# Runtime: 905 ms
# Memory: 33.7 MB

class Solution:
    def latestTimeCatchTheBus(self, B: List[int], A: List[int], C: int) -> int:
        A.sort()
        B.sort()
        #print(A)
        #print(B)
        #ans = A[0] - 1
        ans = 0
        seen = {A[0]}
        i = j = c = 0
        NA = len(A)
        NB = len(B)
        while i < NA and j < NB:
            if c == C:
                j += 1
                c = 0
            if j == NB:
                break
            if A[i] > B[j]:
                if c < C and B[j] not in seen:
                    ans = max(ans, B[j])
                c = 0
                j += 1
            else:
                if A[i] - 1 not in seen:
                    ans = max(ans, A[i] - 1)
                
                
                seen.add(A[i])
                i += 1
                c += 1
        
        if j < NB - 1:
            ans = max(ans, B[-1])
        if c < C and j == NB - 1 and B[-1] not in seen:
            ans = max(ans, B[-1])
        
        return ans
                
            
        
        