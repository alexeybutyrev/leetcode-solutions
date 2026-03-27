# Problem: Find Duplicate File in System
# Language: python3
# Runtime: 112 ms
# Memory: 24.3 MB

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for p in paths:
            s = p.split(" ")
            path = s[0]
            for j in range(1,len(s)):
                x = s[j]
                ind = x.find("(")
                content = x[ind + 1:len(x)-1]
                hm[content].append(path + "/" + x[:ind])
        
        ans = []
        for k in hm:
            if len(hm[k]) > 1:
                ans.append(hm[k])
        return ans