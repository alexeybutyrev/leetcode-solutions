# Problem: Number of Different Integers in a String
# Language: python3
# Runtime: 24 ms
# Memory: 14.1 MB

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ints = set()
        
        s = ""
        for l in word:
            if l.isdigit():
                s += l
            else:
                if s:
                    s = s.lstrip("0")
                    if s:
                        ints.add(s)
                    else:
                        ints.add("0")
                    s = ""
        if s:
            s = s.lstrip("0")
            if s:
                ints.add(s)
            else:
                ints.add("0")
            s = ""
        count = 0
        for w in ints:
            if len(w) > 1 and w[0] == "0":
                continue
            else:
                count += 1
                
        return count