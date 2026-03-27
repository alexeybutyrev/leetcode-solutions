# Problem: Binary Watch
# Language: python3
# Runtime: 1322 ms
# Memory: 19.4 MB

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.ans = set()
        def walk(h,m,c):
            if h < 12 and m <= 59:
                if c == 0:
                    H = str(h)
                    M = str(m)
                    if len(M) == 1:
                        M = '0' + M
                    self.ans.add(H + ':' + M)
                else:
                    # add to hours
                    for i in range(4):
                        if h & (1<<i) == 0:
                            walk(h | (1<<i),m,c-1)
                    
                    # add to mins
                    for i in range(6):
                        if m & (1<<i) == 0:
                            walk(h, m | (1<<i),c-1)
                    
        
        
        walk(0,0,turnedOn)
        return sorted(self.ans)