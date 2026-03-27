# Problem: Maximum Number of Non-Overlapping Substrings
# Language: python3
# Runtime: 812 ms
# Memory: 25.6 MB

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
        begin = {c:i for i,c in reversed(list(enumerate(s)))}
        end   = {c:i for i,c in enumerate(s)}
        
        print(begin, end)
        
        intervals = []
        for c in set(s):
            b,e = begin[c], end[c]
            
            i = b
            while i <= e and b == begin[c]:
                b = min(b, begin[s[i]])
                e = max(e, end[s[i]])
                i += 1
                
            if b == begin[c]:
                intervals.append((e,b))
        
        intervals.sort()
        ans, prev = [], -1

        for e,b in intervals:
            if b > prev:
                ans.append(s[b:e+1])
                
            prev = e
        return ans