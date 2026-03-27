# Problem: Maximum Number of Operations to Move Ones to the End
# Language: python3
# Runtime: 146 ms
# Memory: 20.2 MB

class Solution:
    def maxOperations(self, S: str) -> int:
        count = 0
        ans = 0
        s = []
        for x in S:
            if s and x == '0' and s[-1] == x:
                continue
            else:
                s.append(x)
        
        N = len(s)

        is_zero = []
        p = False
        for x in s[::-1]:
            
            if x == '0':
                p = True
            is_zero.append(p)
        is_zero = is_zero[::-1]
  
        for i,x in enumerate(s):
            if x == '1':
                count += 1
            else:
                if is_zero[i]:
                    ans += count

        return ans

