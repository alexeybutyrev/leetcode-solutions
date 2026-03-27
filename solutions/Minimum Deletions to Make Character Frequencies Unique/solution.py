# Problem: Minimum Deletions to Make Character Frequencies Unique
# Language: python3
# Runtime: 111 ms
# Memory: 17.1 MB

class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        s = set(c.values())
        c = Counter(c.values())
        ans = 0
        for v,k in sorted([(v,k) for k,v in c.items()], reverse=True):
            if v > 1:
                i = k
                while v > 1:
                    if i:
                        i -= 1
                        while i and i in s:
                            i-= 1
                        if i not in s:
                            s.add(i)
                        v -= 1
                        ans += k - i
                            
                    else:
                        ans += k
                        v -= 1
                    
        return ans