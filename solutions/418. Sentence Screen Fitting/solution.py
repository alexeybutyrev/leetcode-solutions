# Problem: Sentence Screen Fitting
# Language: python3
# Runtime: 215 ms
# Memory: 14 MB

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence)+' '
        start, l = 0,len(s)
        for i in range(rows):
            start+=cols
            while s[start % l]!=' ':
                start-=1
            start+=1
        return start//l
                