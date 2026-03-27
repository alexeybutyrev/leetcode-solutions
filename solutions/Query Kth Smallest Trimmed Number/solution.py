# Problem: Query Kth Smallest Trimmed Number
# Language: python3
# Runtime: 1031 ms
# Memory: 15.8 MB

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        dt = {}
        ans = []
        for k,d in queries:
            if d not in dt:
                h = []
                for i,x in enumerate(nums):
                    heappush(h,(x[-d:],i))
                
                dt[d] = h
            
            #print(k,d, dt)
            #print(nsmallest(k,dt[d]))
            ans.append(nsmallest(k,dt[d])[-1][1])
        
        return ans