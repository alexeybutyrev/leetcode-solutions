# Problem: Circular Sentence
# Language: python3
# Runtime: 31 ms
# Memory: 13.8 MB

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        S = sentence.split(" ")
        if " " not in sentence:
            return sentence[0] == sentence[-1]
        
        if S[0][0] != S[-1][-1]:
            return False
        
        for i in range(1,len(S)):
            if S[i-1][-1] != S[i][0]:
                return False
        return True