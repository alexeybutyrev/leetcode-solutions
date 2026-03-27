# Problem: Check if the Sentence Is Pangram
# Language: python3
# Runtime: 56 ms
# Memory: 13.8 MB

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26