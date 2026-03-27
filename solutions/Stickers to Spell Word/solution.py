# Problem: Stickers to Spell Word
# Language: python3
# Runtime: 2362 ms
# Memory: 40.9 MB

class Solution:
    def minStickers(self, W: List[str], target: str) -> int:
        A = []
        NL = 26
        t = [0] * NL
        for w in W:
            l = [0] * NL
            for c in w:
                l[ord(c) - ord('a')] += 1
                t[ord(c) - ord('a')] = 1
            A.append(l)
        T = [0] * NL
        for c in target:
            T[ord(c) - ord('a')] += 1
        
        X = len(A)
        @cache
        def dp(i,state):
            if sum(state) == 0: return 0
            if i >= X: return inf
            
            s1 = dp(i+1,state)
            s2 = inf
            for x,y in zip(state, A[i]):
                if x and y:
                    break
            else:
                return s1
            S = list(state)
            for j,(x,y) in enumerate(zip(state, A[i])):
                if x and y:
                    S[j] = max(0,x-y)
            s2 = 1 + dp(i, tuple(S))
            return min(s1,s2)
        
        ans = dp(0,tuple(T))
        return -1 if ans == inf else ans
            
        