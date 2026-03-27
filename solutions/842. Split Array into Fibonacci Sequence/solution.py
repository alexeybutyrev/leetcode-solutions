# Problem: Split Array into Fibonacci Sequence
# Language: python3
# Runtime: 76 ms
# Memory: 14.6 MB

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        LIMIT = 2 ** 31
        
        N = len(S)
        def dfs(a, b, c, i, ans):
            
            if c is not None and a is not None and b is not None and i == N and int(c) == int(a) + int(b):
                A = ans[:]
                if len(A) < 3:
                    A = [a,b,c]
                else:
                    A = A + [c]
                return (True, A)
            
            if i == N:
                return (False, [])
            
            if b is None:
                if not a.startswith("0") and int(a + S[i]) < LIMIT:
                    a1 = dfs(a + S[i], b, c, i + 1,ans) 
                    if a1[0]:
                        return a1
                
                return dfs(a, S[i], c, i + 1,ans)
            
            if c is None:
                if not b.startswith("0")  and int(b + S[i]) < LIMIT:
                    a1 = dfs(a, b + S[i], c, i + 1,ans) 
                    if a1[0]:
                        return a1
                
                return dfs(a, b, S[i], i + 1,ans)

            
            if int(c) == int(a) + int(b):
                A = ans[:]
                if len(A) < 3:
                    A = [a,b,c]
                else:
                    A = A + [c]
                return dfs(b, c, S[i], i + 1, A)
            else:
                if int(c + S[i]) < LIMIT:
                    return dfs(a, b, c + S[i], i + 1, ans)
                else:
                    return (False, [])
                
        #print(dfs(S[0], None, None, 1, []))
        
        return dfs(S[0], None, None, 1, [])[1]
    