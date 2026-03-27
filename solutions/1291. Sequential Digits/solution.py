# Problem: Sequential Digits
# Language: python3
# Runtime: 24 ms
# Memory: 13.8 MB

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        h = high
        n = 0
        while h:
            h = h // 10
            n+=1
        
        h = low
        m = 0
        while h:
            h = h // 10
            m+=1
        
        s = '123456789'
        res = []
        for window in range(m,n+1):
            for i in range(0,9-window+1):
                num = int(s[i:i+window])
                if num >= low:
                    if num <= high:
                        res.append(num)
                    else:
                        break
                
        return res