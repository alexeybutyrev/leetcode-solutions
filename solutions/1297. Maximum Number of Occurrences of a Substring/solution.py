# Problem: Maximum Number of Occurrences of a Substring
# Language: python3
# Runtime: 3856 ms
# Memory: 125.9 MB

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        B = Counter()
        i = 0
        j = 0
        N = len(s)
        count = 0
        C = Counter()
        while i < N and j < N:
            
            B[s[j]] += 1
            while j - i + 1 > maxSize or len(B) > maxLetters:
                B[s[i]] -= 1
                if not B[s[i]]:
                    del B[s[i]]
                i+=1
                
            copyB = deepcopy(B)
            i1 = i
            j1 = j
            while copyB and maxSize >= j1 - i1 + 1 >= minSize:
                copyB[i1] -= 1
                C[s[i1:j1+1]] += 1
                i1+= 1
            
            j += 1
        
           
        return max(C.values()) if C else 0
        
                