# Problem: Move Pieces to Obtain a String
# Language: python3
# Runtime: 219 ms
# Memory: 16.5 MB

class Solution:
    def canChange(self, S: str, T: str) -> bool:
        N = len(S)
        S = list(S)
        T = list(T)
        
        i = 0
        while i < N:
            #print(i)
            if S[i] == T[i]:
                i+=1
            
            elif S[i] == '_' and T[i] == "L":
                cs = 0
                ct = 0
                while i < N and S[i] in {"_","L"} and T[i] in {"_","L"}:
                    if S[i] == "L":
                        cs += 1
                    if T[i] == "L":
                        ct += 1
                    i += 1
                    if cs > ct:
                        return False
                if cs != ct:
                    return False
                            
            elif S[i] == 'R' and T[i] == "_":
                cs = 0
                ct = 0
                while i < N and S[i] in {"_","R"} and T[i] in {"_","R"}:
                    if S[i] == "R":
                        cs += 1
                    if T[i] == "R":
                        ct += 1
                    i += 1
                    if cs < ct:
                        return False
                if cs != ct:
                    return False
            else:
                return False
                    
                    
                
        return True