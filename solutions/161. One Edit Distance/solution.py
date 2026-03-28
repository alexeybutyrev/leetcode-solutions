# Problem: One Edit Distance
# Language: python3
# Runtime: 28 ms
# Memory: 14 MB

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        
        if l1 < l2:
            s,t = t,s
            l1 = len(s)
            l2 = len(t)

            
        if l1 - l2 >=2:
            return False
        
        c1 = Counter(s)
        c2 = Counter(t)
        

        ans = False
        if l1 == l2:
            for i in range(l1):
                if s[i] != t[i]:
                    if ans:
                        return not ans
                    ans = True
            
            return ans
        else:
            i = 0
            
            while i < l2:
                
                if not ans:
                    if s[i] != t[i]:
                        ans = True
                    else:
                        i+=1
                else:
                    if s[i+1] != t[i]:
                        return False
                    else:
                        i+=1
            if not ans:
                return True
        return ans
            