# Problem: Maximum Number of Moves to Kill All Pawns
# Language: python3
# Runtime: 2678 ms
# Memory: 141.6 MB


# initializing the matrix. 
dp = [[0 for i in range(50)] for j in range(50)]; 
  
@cache
def getsteps(x, y, tx, ty): 
      
    # if knight is on the target 
    # position return 0. 
    if (x == tx and y == ty): 
        return dp[0][0]; 
      
    # if already calculated then return 
    # that value. Taking absolute difference. 
    elif(dp[abs(x - tx)][abs(y - ty)] != 0): 
        return dp[abs(x - tx)][abs(y - ty)]; 
    else: 
  
        # there will be two distinct positions 
        # from the knight towards a target. 
        # if the target is in same row or column 
        # as of knight then there can be four 
        # positions towards the target but in that 
        # two would be the same and the other two 
        # would be the same. 
        x1, y1, x2, y2 = 0, 0, 0, 0; 
  
        # (x1, y1) and (x2, y2) are two positions. 
        # these can be different according to situation. 
        # From position of knight, the chess board can be 
        # divided into four blocks i.e.. N-E, E-S, S-W, W-N . 
        if (x <= tx): 
            if (y <= ty): 
                x1 = x + 2; 
                y1 = y + 1; 
                x2 = x + 1; 
                y2 = y + 2; 
            else: 
                x1 = x + 2; 
                y1 = y - 1; 
                x2 = x + 1; 
                y2 = y - 2; 
  
        elif (y <= ty): 
            x1 = x - 2; 
            y1 = y + 1; 
            x2 = x - 1; 
            y2 = y + 2; 
        else: 
            x1 = x - 2; 
            y1 = y - 1; 
            x2 = x - 1; 
            y2 = y - 2; 
  
        # ans will be, 1 + minimum of steps 
        # required from (x1, y1) and (x2, y2). 
        dp[abs(x - tx)][abs(y - ty)] = min(getsteps(x1, y1, tx, ty), getsteps(x2, y2, tx, ty)) + 1; 
  
        # exchanging the coordinates x with y of both 
        # knight and target will result in same ans. 
        dp[abs(y - ty)][abs(x - tx)] = dp[abs(x - tx)][abs(y - ty)]; 
        return dp[abs(x - tx)][abs(y - ty)]; 



@cache
def find(x,y,tx,ty):
    # size of chess board n*n 
    n = 50; 
    
    # (Exception) these are the four corner points 
    # for which the minimum steps is 4. 
    if ((x == 1 and y == 1 and tx == 2 and ty == 2) or
            (x == 2 and y == 2 and tx == 1 and ty == 1)): 
        ans = 4; 
    elif ((x == 1 and y == n and tx == 2 and ty == n - 1) or
        (x == 2 and y == n - 1 and tx == 1 and ty == n)): 
        ans = 4; 
    elif ((x == n and y == 1 and tx == n - 1 and ty == 2) or
        (x == n - 1 and y == 2 and tx == n and ty == 1)): 
        ans = 4; 
    elif ((x == n and y == n and tx == n - 1 and ty == n - 1) 
        or (x == n - 1 and y == n - 1 and tx == n and ty == n)): 
        ans = 4; 
    else: 
  
        # dp[a][b], here a, b is the difference of 
        # x & tx and y & ty respectively. 
        dp[1][0] = 3; 
        dp[0][1] = 3; 
        dp[1][1] = 2; 
        dp[2][0] = 2; 
        dp[0][2] = 2; 
        dp[2][1] = 1; 
        dp[1][2] = 1; 
  
        ans = getsteps(x, y, tx, ty); 
  
    return ans



class Solution:
    def maxMoves(self, kx: int, ky: int, A: List[List[int]]) -> int:
        A = [(x+1,y+1)for x,y in A]
        kx+=1
        ky+=1
        N = len(A)
        T = (1 << N) - 1
        
        @cache
        def solve(x,y, mask, a):
            if mask == T: return 0
            if a:
                ans = -1
                for i in range(N):
                    if (1 << i) & mask == 0:
                        c = find(x,y,A[i][0], A[i][1])
                        ans = max(ans, c + solve(A[i][0],A[i][1], mask | (1 << i), not a))
            else:
                ans = inf
                for i in range(N):
                    if (1 << i) & mask == 0:
                        c = find(x,y,A[i][0], A[i][1])
                        ans = min(ans, c + solve(A[i][0],A[i][1], mask | (1 << i), not a))
            return ans


        
        return solve(kx, ky, 0, True)