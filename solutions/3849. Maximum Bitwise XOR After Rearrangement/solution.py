# Problem: Maximum Bitwise XOR After Rearrangement
# Language: python3
# Runtime: 1015 ms
# Memory: 22.5 MB

class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        c = Counter(t)
        ans = ""
        for x in s:
            if x == '0':
                if c['1']:
                    c['1'] -= 1
                    ans += '1'
                else:
                    c['0'] -= 1
                    ans += '0'
            else:
                if c['0']:
                    c['0'] -= 1
                    ans += '1'
                else:
                    c['1'] -= 1
                    ans += '0'

        return ans
                
                    