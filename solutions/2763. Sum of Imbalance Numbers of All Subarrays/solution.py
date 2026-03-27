# Problem: Sum of Imbalance Numbers of All Subarrays
# Language: python3
# Runtime: 420 ms
# Memory: 16.5 MB

class Solution:
    def sumImbalanceNumbers(self, A: List[int]) -> int:
        N = len(A)
        
        ans = 0
        # left boundary loop
        for i in range(N):
            count = 0
            seen = {A[i]}
            mn = mx = A[i]
            count = 0
            # right boundary loop
            for x in A[i+1:]:
                if x in seen:
                    ans+=count
                    continue
                
                seen.add(x)
                if x+1 in seen and x-1 in seen:
                    # union 2 groups
                    count -=1
                elif x+1 not in seen and x-1 not in seen:
                    count +=1
                    
                ans += count
        return ans