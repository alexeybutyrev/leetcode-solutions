# Problem: Check if the Sentence Is Pangram
# Language: python3
# Runtime: 48 ms
# Memory: 14.4 MB

class Solution:
    def checkIfPangram(self, S: str) -> bool:
        for i in range(26):
            l = chr(i + ord('a'))
            if l not in S:
                return False
        return True