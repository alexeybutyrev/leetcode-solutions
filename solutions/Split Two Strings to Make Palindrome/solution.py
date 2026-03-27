# Problem: Split Two Strings to Make Palindrome
# Language: python3
# Runtime: 128 ms
# Memory: 15.2 MB

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        if len(a) == 1:
            return True
        
        def pali(A, i, j):
            if i >= j: return True
            for k in range(j -i+ 1):
                if A[i+k] != A[j-k]: return False
            return True
        
        
        def check(a,b):
            n = len(a)
            i, j = 0, n - 1
            while i < j  and a[i] == b[j]:
                i+=1
                j-=1
            if pali(a, i, j) or pali(b, i, j):
                return True
        
            
        return check(a,b) or check(b,a)