# Problem: Range Addition
# Language: python3
# Runtime: 181 ms
# Memory: 23 MB

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        c = Counter()
        for l,r,v in updates:
            c[l] += v
            c[r+1] -= v
        
        x = 0
        ans = []
        for i in range(length):
            x += c[i]
            ans.append(x)
        return ans
            