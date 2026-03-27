# Problem: Flip String to Monotone Increasing
# Language: python3
# Runtime: 68 ms
# Memory: 26.7 MB

from collections import Counter
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        S = S.lstrip("0")
        S = S.rstrip("1")
        
        if not S:
            return 0
        
        c = Counter(S)
        n = len(S)

        if "0" not in c:
            return c["1"]
        
        if "1" not in c:
            return c["0"]
        
        stack = []
        curr = 1
        count = 0
        for l in S:
            if (l == "0" and curr == 0) or (l == "1" and curr == 1):
                count +=1
            else:
                stack.append((curr,count))
                count = 1
                if l == "1":
                    curr = 1
                else:
                    curr = 0  
        
        stack.append((curr, count))
        
        n = len(stack)
        def count(i, nzeros):
            if i == n:
                return 0
            if stack[i][0] == 1:
                return min(stack[i][1] + count(i+1,nzeros), nzeros)
            else:
                return count(i+1,nzeros-stack[i][1])
        
        return count(0,c['0'])
        
        
        