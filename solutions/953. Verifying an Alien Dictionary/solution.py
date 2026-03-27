# Problem: Verifying an Alien Dictionary
# Language: python3
# Runtime: 39 ms
# Memory: 13.9 MB

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: list(map(order.index, w)))