# Problem: Find the Power of K-Size Subarrays I
# Language: python3
# Runtime: 65 ms
# Memory: 16.9 MB

class Solution:
    def resultsArray(self, A: List[int], k: int) -> List[int]:
        
        Q = deque()
        for i in range(k):
            Q.append(A[i])
        ans = []
        
        
        def check(Q):
            for j in range(1,k):
                if Q[j] != Q[j-1] + 1:
                    return False
            return True
        
        if check(Q):
            ans.append(Q[-1])
        else:
            ans.append(-1)
        
        for j in range(k, len(A)):
            Q.popleft()
            Q.append(A[j])
            
            if check(Q):
                ans.append(Q[-1])
            else:
                ans.append(-1)
        return ans
        
        