# Problem: Counting Elements
# Language: python3
# Runtime: 32 ms
# Memory: 13.9 MB

class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        hm = dict()
        
        for a in arr:
            if a in hm:
                hm[a] += 1
            else:
                hm[a] = 1

        count = 0
        for e in arr:
            if e+1 in hm and hm[e+1] != 0:
                #hm[e+1] -= 1
                count += 1
                
        return count