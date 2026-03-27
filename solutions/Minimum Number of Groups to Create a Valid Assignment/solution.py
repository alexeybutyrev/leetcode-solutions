# Problem: Minimum Number of Groups to Create a Valid Assignment
# Language: python3
# Runtime: 840 ms
# Memory: 34.6 MB

class Solution:
    def minGroupsForValidAssignment(self, A: List[int]) -> int:
        
        
        c = Counter(A)
        mn = min(c.values())
        if len(c) == 1:
            return 1
        
        def check(x):
            
            count = 0
            for a in c.values():
                groups = a // x
                rem = a % x
                
                if rem > groups:
                    return inf
                
                count += groups - (groups - rem) // (x+1)
            return count
        
        ans = inf
        for x in range(1,mn+1):
            curr = check(x)
            ans = min(ans,curr)
        
        return ans
        
            
        