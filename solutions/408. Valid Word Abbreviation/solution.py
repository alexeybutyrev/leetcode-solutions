# Problem: Valid Word Abbreviation
# Language: python3
# Runtime: 27 ms
# Memory: 16.3 MB

class Solution:
    def validWordAbbreviation(self, A: str, B: str) -> bool:
        N,M = len(A),len(B)
        
        i = j = 0
        
        while i < N and j <M:
            if A[i] == B[j]:
                j += 1
                i +=1 
                continue
            else:
                if B[j].isdigit():
                    if B[j] == '0': return False
                    d = 0
                    while j < M and B[j].isdigit():
                        d *= 10
                        d += int(B[j])
                        j += 1
                    i += d
                    if i > N: return False
                else:
                    return False
                
        return i == N and j == M
                