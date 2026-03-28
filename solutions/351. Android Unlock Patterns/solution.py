# Problem: Android Unlock Patterns
# Language: python3
# Runtime: 1224 ms
# Memory: 14.4 MB

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        not_check_digits = set([2,4,5,6,8])
        
        def check(d, nd, seen):
            if d in seen:
                return False
            
            
            
            if nd in not_check_digits or d in not_check_digits:
            
                if (d == 4 and nd == 6) or (d == 6 and nd == 4):
                    return 5 in seen
                
                if (d == 8 and nd == 2) or (d == 2 and nd == 8):
                    return 5 in seen
                
                return True
            
            
            if d == 3 and nd == 7 or d == 7 and nd == 3:
                return 5 in seen
            
            if d == 1 and nd == 3 or d == 3 and nd == 1:
                return 2 in seen
            
            if d == 1 and nd == 7 or d == 7 and nd == 1:
                return 4 in seen
            
            
            
            if d == 1 and nd == 9 or d == 9 and nd == 1:
                return 5 in seen
            
            if d == 3 and nd == 7 or d == 7 and nd == 3:
                return 5 in seen
            
            if d == 1 and nd == 3 or d == 3 and nd == 1:
                return 2 in seen
            
            if d == 1 and nd == 7 or d == 7 and nd == 1:
                return 4 in seen
            
            if d == 3 and nd == 9 or d == 9 and nd == 3:
                return 6 in seen
            
            if d == 7 and nd == 9 or d == 9 and nd == 7:
                return 8 in seen
            
        
        count = 0
        def dfs(seen, nd):
            nonlocal count
            if len(seen) <= n:
                if len(seen) >= m:
                    count += 1
                if len(seen) < n:
                    for d in range(1,10):
                        if check(d, nd, seen):
                            dfs(seen | {d}, d)
                    
        
        for d in range(1,10):
            dfs({d},d)
        
        return count