# Problem: Find Winner on a Tic Tac Toe Game
# Language: python3
# Runtime: 85 ms
# Memory: 14.3 MB

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = [[inf] * 3 for _ in range(3)]
        
        def check(A):
            s0 = 0
            for r in A:
                s = sum(r)
                if s == 3:
                    return 1
                elif s == -3:
                    return -1
                s0 += s
            
            for r in zip(*A):
                s = sum(r)
                if s == 3:
                    return 1
                elif s == -3:
                    return -1
            
            s1 = s2 = 0
            for i in range(3):
                s1 += A[i][i]
                s2 += A[i][2-i]
            
            if s1 == 3 or s2 == 3: return 1
            if s2 == -3 or s1 == -3: return -1
            
            
            return 0 if s0 == inf else 3
        
        for turn, (i,j) in enumerate(moves):
            if turn & 1:
                A[i][j] = -1
            else:
                A[i][j] = 1
            val = check(A)
            #print(val)
            if val != 0:
                if val == 1:
                    return "A"
                elif val == -1:
                    return "B"
                elif val == 3:
                    return "Draw"
        #print(A)        
        return "Pending"