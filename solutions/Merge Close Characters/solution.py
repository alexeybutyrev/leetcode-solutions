# Problem: Merge Close Characters
# Language: python3
# Runtime: 47 ms
# Memory: 19.4 MB

class Solution:
    def mergeCharacters(self, S: str, k: int) -> str:
        A = list(S)
        
        def f(A):
            N = len(A)
            is_del = False
            for i in range(N):
                if i == len(A):
                    break
    
                for j in range(i+1,i + k+1):
                    if j < len(A):
                    
                        if A[j] == A[i]:
                            print(A)
                            A.pop(j)
                            is_del = True
                    else:
                        break
                if is_del:
                    return A,is_del
                                        
            return A,is_del

        B, id = f(A)
        while id:
            B, id = f(B[:])
        return "".join(B)

        