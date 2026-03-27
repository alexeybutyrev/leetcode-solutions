# Problem: Zigzag Conversion
# Language: python3
# Runtime: 164 ms
# Memory: 21.2 MB

class Solution:
    def convert(self, s: str, NR: int) -> str:
        N = len(s)
        A = [[''] * N for _ in range(NR)]
        
        def make_ans(A):
            ans = ""
            for r in A:
                ans += "".join(r).replace(' ','')
            return ans
        
        k = 0
        j = 0
        i = 0
        while k < N:
            
            for i in range(NR):
                A[i][j] = s[k]
                k += 1
                if k == N:
                    return make_ans(A)
            
            for l in range(NR-2):
                i-=1
                j+=1
                A[i][j] = s[k]
                
                k+=1
                if k == N:
                    return make_ans(A)
            
            j+=1