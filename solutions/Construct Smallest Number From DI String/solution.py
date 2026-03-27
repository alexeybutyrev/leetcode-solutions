# Problem: Construct Smallest Number From DI String
# Language: python3
# Runtime: 399 ms
# Memory: 17.8 MB

class Solution:
    def smallestNumber(self, A: str) -> str:
        N = len(A)
        self.ans = '9' * N
        def walk(i,ans):
            if i == N:
                self.ans = min(ans, self.ans)
            else:
                #if (A[i] == "I" and ans[-1] == "9") or (A[i] == "D" and ans[-1] == "1"):
                #    continue
                s = set(ans)
                if A[i] == "I":
                    for d in range(int(ans[-1]) + 1,10):
                        if str(d) not in s:
                            walk(i+1,ans + str(d))
                else:
                    for d in range(int(ans[-1]),0,-1):
                        if str(d) not in s:
                            walk(i+1,ans + str(d))
            
        for d in range(1,10):
            walk(0,str(d))
            
        return self.ans