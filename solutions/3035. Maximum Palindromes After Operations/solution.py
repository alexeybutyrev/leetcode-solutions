# Problem: Maximum Palindromes After Operations
# Language: python3
# Runtime: 181 ms
# Memory: 17.5 MB

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        words.sort(key = len)
        
        c = Counter()
        for x in words:
            c += Counter(x)
        
        o = e = 0
        for k,v in c.items():
            if v & 1:
                e += 1
                o += (v - 1) 
            else:
                o += v

        for i,x in enumerate(words):

            l = len(x)
            if l & 1:
                if e:
                    l -= 1
                    if o < l:
                        return i
                else:
                    o -= 1
                    l -= 1
                    if o < l:
                        return i
                o -= l
            else:
                if o < l:
                    return i
                o -= l
        return len(words)
            