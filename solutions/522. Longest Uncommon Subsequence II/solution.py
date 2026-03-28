# Problem: Longest Uncommon Subsequence II
# Language: python3
# Runtime: 308 ms
# Memory: 18.4 MB

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        A = defaultdict(set)
        for i,word in enumerate(strs):
            s = {""}
            for l in word:
                s |= {w + l for w in s}
            A[i] = s
        
        N = len(strs)
        ans = -1
        for i in range(N):
            s = deepcopy(A[i])
            for j in range(N):
                if i != j:
                    s -= A[j]
            for w in s:
                ans = max(ans,len(w))
        
        return ans
                