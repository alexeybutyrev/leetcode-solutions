# Problem: Bold Words in String
# Language: python3
# Runtime: 52 ms
# Memory: 14.4 MB

from collections import deque
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        
        intervals = []
        for w in words:
            ind = S.find(w)
            nw = len(w)
            while ind >= 0:
                intervals.append([ind, ind + nw])
                ind = S.find(w, ind+1)
        
        if not intervals:
            return S
        intervals.sort()
        

        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        
        begin = list(map(lambda x: x[0], res))
        end   = list(map(lambda x: x[1], res))

        result = ""
        for i in range(len(S)):
            if i in begin:
                result += "<b>"
            
            if i in end:
                result += "</b>"
            result += S[i]
        if len(S) in end:
            result += "</b>"
            
        return result
    
        
        