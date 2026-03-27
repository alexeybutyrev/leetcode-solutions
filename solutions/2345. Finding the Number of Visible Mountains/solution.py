# Problem: Finding the Number of Visible Mountains
# Language: python3
# Runtime: 1778 ms
# Memory: 72.3 MB

class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        
        
        bl = [-y + x for x,y in peaks]
        br = [y + x for x,y in peaks]
        
        
        p = [(l,r) for l,r in zip(bl,br)]
        
        c = Counter()
        for x,y in p:
            c[(x,y)] += 1
        
        stack = []
        
        for l,r in sorted(p, key = lambda x: (x[0],-x[1])):
            if stack:
                if stack[-1][0] < l and stack[-1][1] < r:
                    stack.append((l,r))
                    
            else:
                stack.append((l,r))
        
        ans = 0
        for x,y in stack:
            if c[(x,y)] == 1:
                ans+= 1
        return ans