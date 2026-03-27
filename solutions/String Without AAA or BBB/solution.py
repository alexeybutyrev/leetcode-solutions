# Problem: String Without AAA or BBB
# Language: python3
# Runtime: 28 ms
# Memory: 14.1 MB

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ca = cb = 0
        s = ""
        while A and B:
            if (A > B and ca < 2):
                ca += 1
                cb = 0
                s+= "a"
                A -= 1
            elif (A < B and cb < 2):
                ca = 0
                cb += 1
                s += 'b'
                B -=1
            else:
                if (cb > ca):
                    ca += 1
                    cb = 0
                    s+= "a"
                    A -= 1
                else:
                    ca = 0
                    cb += 1
                    s += 'b'
                    B -=1
        
        if A:
            s += "a"*A
        
        if B:
            s += "b"*B
        
        return s
