# Problem: Substring with Concatenation of All Words
# Language: python3
# Runtime: 3540 ms
# Memory: 20.6 MB

class Solution:
    def findSubstring(self, S: str, W: List[str]) -> List[int]:
        N = len(S)
        NW = len(W)
        
        C = Counter(W)
        len_all_words = sum( len(w) * c for w,c in C.items())
        
        
        def dfs(i,counter):
            if sum(counter.values()) == 0:
                return True
            
            for w in counter:
                if counter[w] and S[i:i+len(w)] == w:
                    counter[w] -= 1
                    if dfs(i + len(w), counter):
                        return True
                    counter[w] += 1
            return False
        
        ans = []
        for i in range(N):
            if N - i >= len_all_words and dfs(i, deepcopy(C)):
                ans.append(i)
        return ans