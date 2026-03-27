# Problem: Add Bold Tag in String
# Language: python3
# Runtime: 48 ms
# Memory: 16 MB

import re
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # s = "abcxyz123", words = ["abc","123"]
        
        intervals = []
        for w in words:
            ind = 0
            ind = s.find(w,ind)
            #if w == s:
            #    return "<b>" + s + "</b>"
            while ind >= 0:
                intervals.append([ind, ind + len(w)])
                ind = s.find(w,ind+1)
       
        # merge intervals
        
        if not intervals:
            return s
        intervals.sort(key = lambda x: (x[0],-x[1]))
        #print(intervals)
        B = []
        for i, (a,b) in enumerate(intervals):
            if B and B[-1][1] >= a:
                B[-1][1] = max(b, B[-1][1])
            else:
                B.append([a,b])
        #print(B)
        hm = {}
        for a,b in B:
            hm[a] = "<b>"
            hm[b] = "</b>"
        
        ans = ""
        for i,l in enumerate(s):
            if i in hm:
                ans += hm[i]
            ans += l
        if len(s) in hm:
            ans += hm[len(s)]
            
        return ans