# Problem: Find Words Containing Character
# Language: python3
# Runtime: 65 ms
# Memory: 16.4 MB

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i,w in enumerate(words) if x in w]