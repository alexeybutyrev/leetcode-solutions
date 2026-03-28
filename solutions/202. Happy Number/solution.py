# Problem: Happy Number
# Language: python3
# Runtime: 40 ms
# Memory: 13.6 MB

class Solution:
    def isHappy(self, n: int) -> bool:
       s = set()
       s.add(n)
       while 1!= n:
        n = sum(list(map(lambda x: int(x)*int(x), list(str(n)))))
        if n in s: 
                return False
        s.add(n)
            
       return True