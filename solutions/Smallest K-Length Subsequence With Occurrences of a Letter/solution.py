# Problem: Smallest K-Length Subsequence With Occurrences of a Letter
# Language: python3
# Runtime: 680 ms
# Memory: 15.3 MB

class Solution:
    def smallestSubsequence(self, S: str, K: int, L: str, repetition: int) -> str:
        
        N = len(S)
        to_del = N - K
        bonus_dels = S.count(L) - repetition
        
        ans = []
        for i, l in enumerate(S):
            
            while ans and to_del and (ans[-1] != L or bonus_dels) and l < ans[-1]:
                to_del -= 1
                bonus_dels -= ans.pop() == L
            
            ans.append(l)
        
        for j in range(len(ans) - 1, -1, -1):
            if to_del and (ans[j] != L or bonus_dels):
                to_del -= 1
                bonus_dels -= ans[j] == L
                ans[j] = ""
        return "".join(ans)