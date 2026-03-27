# Problem: Sort Vowels in a String
# Language: python3
# Runtime: 86 ms
# Memory: 20.2 MB

class Solution:
    def sortVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u']
        V = [x.upper() for x in v]
        hm = {}
        rhm = {}
        for i in range(5):
            hm[V[i]] = i
            hm[v[i]] = i+5
            rhm[i] = V[i]
            rhm[i+5] = v[i]
        
        A = []
        for x in s:
            if x in hm:
                A.append(hm[x])
        A.sort(reverse=True)
        
        ans = ""
        for x in s:
            if x in hm:
                ans += rhm[A.pop()]
            else:
                ans += x
        return ans