# Problem: Maximum Rows Covered by Columns
# Language: python3
# Runtime: 64 ms
# Memory: 14 MB

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        A = []
        ans = 0
        c = Counter()
        for r in mat:
            sr = sum(r)
            if sr == 0:
                ans += 1
            elif sr <= cols:
                A.append(r)
                x = int("".join(list(map(str,r))),2)
                c[x] += 1      
        if not A:
            return ans
        
        n = len(A[0])
        
        def backtrack(s):
            if len(s) == cols:
                x = 0
                for i in s:
                     x |= (1<<i)
                a = 0
                for k in c:
                    if k & x == k:
                        a += c[k]
                return a
            
            ans = 0
            for i in range(s[-1]+1,n):
                ans = max(ans,backtrack(s + [i]))
            return ans
        return ans + max(backtrack([i]) for i in range(n))
    
            
        
        la = 0
        for p in permutations(range(n),cols):
            
            x = 0
            for i in p:
                x |= (1<<i)
            a = 0 
            for k in c:
                if k & x == k:
                    a += c[k]
            la = max(a,la)

        return ans + la
                