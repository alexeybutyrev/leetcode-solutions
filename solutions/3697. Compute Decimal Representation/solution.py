# Problem: Compute Decimal Representation
# Language: python3
# Runtime: 0 ms
# Memory: 18 MB

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        i = 0
        while n:
            x = n % 10
            n -= x
            n //= 10
            if x:
                ans.append(x * 10**(i))
            i+=1
        return ans[::-1]