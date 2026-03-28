# Problem: Fraction Addition and Subtraction
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def fractionAddition(self, S: str) -> str:
        if not S:
            return S
        
        if S[0] != "-":
            S = "+" + S
            

        n = d = ""
        nums = []
        denums = []
        for i,l in enumerate(S):
            if l in ["+","-"]:
                if d:
                    denums.append(int(d))
                d = ""
                n = l
            elif l == "/":
                nums.append(int(n))
                n = ""
            else:
                if n:
                    n += l
                else:
                    d += l
                
        
        denums.append(int(d))

        p = 1
        for n in range(1,10):
            p *= n
        
        s = 0
        for i, n in enumerate(nums):
            if n != 0:
                s += n * (p // denums[i])
        
        for i in range(11,0,-1):
            for i in range(11,0,-1):
                if s % i == 0 and p % i == 0:
                    s //= i
                    p //= i
                
        return str(s) + "/" + str(p)
        