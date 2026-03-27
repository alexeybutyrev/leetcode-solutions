# Problem: Generate Binary Strings Without Adjacent Zeros
# Language: python3
# Runtime: 286 ms
# Memory: 18 MB

class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        ans = []
        for x in range(1<<n):
            s = bin(x)[2:]
            c = '0' * (n - len(s)) + s
            for i in range(1,n):
                if c[i] == c[i-1] == '0':
                    break
            else:
                ans.append(c)
        return ans