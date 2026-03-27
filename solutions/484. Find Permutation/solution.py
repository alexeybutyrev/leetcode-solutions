# Problem: Find Permutation
# Language: python3
# Runtime: 80 ms
# Memory: 14.9 MB

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        #if not s:
        #    return [1]
        
        n = len(s)
        res = list(range(1,n+2))
        i = 0
        while i < n:
            if s[i] == "D":
                j = i
                while j < n and s[j] == "D":
                    j+=1
                res[i:j+1] = res[i:j+1][::-1]
                i = j+1
            else:
                i+=1
        return res
        
        
                    