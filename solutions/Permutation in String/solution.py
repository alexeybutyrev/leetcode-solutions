# Problem: Permutation in String
# Language: python3
# Runtime: 64 ms
# Memory: 13.7 MB

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
                
        n1 = len(s1)
        n2 = len(s2)
        
        if n2 < n1:
            return False
        
        if n2 == n1:
            return sorted(s1) == sorted(s2)
        
        start, end = ord('a'), ord('z')
        hm = {chr(i): 0 for i in range(start,end+1)}
        
        base_hm = {chr(i): 0 for i in range(start,end+1)}
        for s in s1:
            base_hm[s] +=1
        
            
        for i in range(n2):
            if i >= n1:
                hm[s2[i - n1]] = max(0, hm[s2[i - n1]]-1)
            
            if s2[i] in s1:
                hm[s2[i]] += 1
            
            if base_hm == hm:
                return True
            
        return False
    