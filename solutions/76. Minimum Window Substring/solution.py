# Problem: Minimum Window Substring
# Language: python3
# Runtime: 152 ms
# Memory: 14.8 MB

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)
        
        c = Counter()
        used = set()
        
        ans = ""
        N = len(s)
        l = inf
        i = 0
        j = 0
        while i < N and j < N:
            c[s[j]] += 1
            if s[j] in ct and c[s[j]] >= ct[s[j]]:
                used.add(s[j])                    
                while len(used) == len(ct):
                    if l > j - i + 1:
                        ans = s[i:j+1]
                        l = j - i + 1    

                    c[s[i]] -= 1
                        
                    
                    if s[i] in ct and c[s[i]] < ct[s[i]]:
                        used.remove(s[i])
                    i += 1
                
            j+=1
        
        return ans
    