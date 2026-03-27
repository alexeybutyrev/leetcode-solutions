# Problem: Minimum Time to Revert Word to Initial State II
# Language: python3
# Runtime: 1516 ms
# Memory: 17.7 MB

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n=len(word)
        for i in range(k,n+1,k):
            if word[i:]==word[:-i]:
                return i//k
        return (n+k-1)//k
        
        