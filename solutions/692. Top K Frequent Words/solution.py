# Problem: Top K Frequent Words
# Language: python3
# Runtime: 106 ms
# Memory: 14.1 MB

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return list(map(lambda x: x[1], sorted([(-v,k) for k,v in Counter(words).items()])))[:k]