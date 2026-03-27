# Problem: Find and Replace Pattern
# Language: python3
# Runtime: 37 ms
# Memory: 13.8 MB

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:        
        ans = []
        for w in words:
            hm1, hm2 = {}, {}
            for l1,l2 in zip(pattern, w):
                if l2 in hm1 and hm1[l2] != l1 or (l1 in hm2 and hm2[l1] != l2):
                    break
                hm1[l2] = l1
                hm2[l1] = l2
                
                
            else:
                ans.append(w)
                
        return ans