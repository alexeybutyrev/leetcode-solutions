# Problem: Knight Dialer
# Language: python3
# Runtime: 1040 ms
# Memory: 14 MB

class Solution:
    def knightDialer(self, n: int) -> int:
        map_move = dict()
        map_move[0] = [4,6]
        map_move[1] = [6,8]
        map_move[2] = [7,9]
        map_move[3] = [4,8]
        map_move[4] = [3,9,0]
        map_move[5] = []
        map_move[6] = [7,1,0]
        map_move[7] = [6,2]
        map_move[8] = [1,3]
        map_move[9] = [4,2]
        
        
        dp = [1] * 10
        
        for i in range(n-1):
            dp2 = [0] * 10
            for j,count in enumerate(dp):
                for l in map_move[j]:
                    dp2[l] += count
            dp = dp2
        

        
        MOD = 10**9 + 7
        return sum(dp) % MOD
        
            