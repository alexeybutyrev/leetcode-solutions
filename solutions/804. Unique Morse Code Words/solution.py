# Problem: Unique Morse Code Words
# Language: python3
# Runtime: 32 ms
# Memory: 14.2 MB

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = set()
        for w in words:
            cw = ""
            for l in w:
                cw += code[ord(l) - ord('a')]
            res.add(cw)
        
        return len(res)