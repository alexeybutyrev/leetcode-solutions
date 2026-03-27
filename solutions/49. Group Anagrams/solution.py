# Problem: Group Anagrams
# Language: python3
# Runtime: 83 ms
# Memory: 22.3 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        def t(x):
            A = [0] * 26
            for l in x:
                A[ord(l) - ord('a')] += 1
            return tuple(A)
        d = defaultdict(list)
        for x in strs:
            d[t(x)].append(x)
        
        return d.values()