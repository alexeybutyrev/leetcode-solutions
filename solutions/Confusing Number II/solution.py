# Problem: Confusing Number II
# Language: python3
# Runtime: 4960 ms
# Memory: 14.3 MB

class Solution:
    def confusingNumberII(self, N: int) -> int:
        m = {} 
        m['0'] = '0'
        m['1'] = '1'
        m['6'] = '9'
        m['8'] = '8'
        m['9'] = '6'
        ks = list(m.keys())

        count = 0
        
        def walk(b):
            nonlocal count
            for k in ks:
                b0 = b + k
                if b0[0] != '0' and int(b0) <= N :
                    ts = ""
                    for j in b0:
                        ts = m[j] + ts
                    if b0 != ts:
                        count += 1
                    walk(b0)
                    
        walk("")
        return count