# Problem: Mark Elements on Array by Performing Queries
# Language: python3
# Runtime: 1209 ms
# Memory: 50.3 MB

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        Q = []
        S = 0 
        for i,x in enumerate(nums):
            heappush(Q, (x,i))
            S += x
            
        seen = set()
        
        
        ans = [0] * len(queries)
        for j,(i, k) in enumerate(queries):
            if i not in seen:
                seen.add(i)
                S -= nums[i]
                
            
            while Q and k:
                x,y = heappop(Q)
                if y not in seen:
                    seen.add(y)
                    S-=x
                    k -= 1
            ans[j] = S
                
        return ans
            