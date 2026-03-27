# Problem: Construct Uniform Parity Array II
# Language: python3
# Runtime: 55 ms
# Memory: 35.5 MB

class Solution:
    def uniformArray(self, A: list[int]) -> bool:
        
        mo = inf
        me = inf
        for x in A:
            if x & 1:
                mo = min(x, mo)
            else:
                me = min(x, me)

        if mo == inf: return True

        if me < mo: return False
        return True