# Problem: Partition Labels
# Language: python3
# Runtime: 40 ms
# Memory: 14.2 MB

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {l:i for i, l in enumerate(S)}
        
        start = j = 0 
        res = []
        for i, l in enumerate(S):
            j = max(last[l],j)
            if i == j:
                res.append(j - start + 1)
                start = i + 1
        return res