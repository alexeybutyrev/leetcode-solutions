# Problem: Palindrome Pairs
# Language: python3
# Runtime: 576 ms
# Memory: 19.6 MB

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        P = defaultdict(set)
        S = defaultdict(set)
        
        is_pali = lambda x: x == x[::-1]
        
        for i,w in enumerate(words):
            for j in range(len(w) + 1):
                s, p = w[:j], w[j:]
                if is_pali(s):
                    P[p].add(i)
                
                if is_pali(p):
                    S[s].add(i)
                
                
        ans = set()
        for i,w in enumerate(words):
            if w[::-1] in P:
                for j in P[w[::-1]]:
                    if j != i:
                        ans.add((i,j))
            
            if w[::-1] in S:
                for j in S[w[::-1]]:
                    if j != i:
                        ans.add((j,i))
        
        return ans