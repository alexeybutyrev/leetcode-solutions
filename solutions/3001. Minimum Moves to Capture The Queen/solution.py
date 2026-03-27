# Problem: Minimum Moves to Capture The Queen
# Language: python3
# Runtime: 43 ms
# Memory: 17.5 MB

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        
        x,y = c,d
        for i in range(9):
            x += 1
            y += 1
            if (x,y) == (a,b): break
            if (x,y) == (e,f): return 1
        
        x,y = c,d
        for i in range(9):
            x -= 1
            y -= 1
            if (x,y) == (a,b): break
            if (x,y) == (e,f): return 1
        
        x,y = c,d
        for i in range(9):
            x -= 1
            y += 1
            if (x,y) == (a,b): break
            if (x,y) == (e,f): return 1
        
        x,y = c,d
        for i in range(9):
            x += 1
            y -= 1
            if (x,y) == (a,b): break
            if (x,y) == (e,f): return 1
            
        x,y = a,b
        for i in range(9):
            x += 1
            if (x,y) == (c,d): break
            if (x,y) == (e,f): return 1

        x,y = a,b
        for i in range(9):
            x -= 1
            if (x,y) == (c,d): break
            if (x,y) == (e,f): return 1

        x,y = a,b
        for i in range(9):
            y += 1
            if (x,y) == (c,d): break
            if (x,y) == (e,f): return 1

        x,y = a,b
        for i in range(9):
            y -= 1
            if (x,y) == (c,d): break
            if (x,y) == (e,f): return 1
            
        return 2
    