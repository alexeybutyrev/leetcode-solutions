# Problem: Group Shifted Strings
# Language: python3
# Runtime: 48 ms
# Memory: 17.4 MB

class Solution:
    def groupStrings(self, S: List[str]) -> List[List[str]]:
        @cache
        def is_shifted(a,b):
            if len(a) != len(b): return False
            if len(a) == 1: return True
            if a[0] == b[0]: return a == b
            if ord(a[0]) < ord(b[0]):
                a,b = b,a
            d = ord(a[0]) - ord(b[0])
            for x,y in zip(a,b):
                x,y = ord(x), ord(y)
                if (x - y) % 26 != d:
                    return False
            return True
        
        c = Counter(S)
        N = len(S)
        ans = []
        seen = set()
        for i in range(N):
            if c[S[i]]:
                lans = [S[i]]
                c[S[i]] -= 1
                for j in range(i+1,N):
                    if c[S[j]] and is_shifted(S[i], S[j]):
                        c[S[j]] -= 1
                        lans.append(S[j])
                ans.append(lans)
        return ans
            