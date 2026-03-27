# Problem: Number of Valid Clock Times
# Language: python3
# Runtime: 77 ms
# Memory: 13.8 MB

class Solution:
    def countTime(self, time: str) -> int:
        max_minutes = 24 * 60
        
        def check(time):
            hh,mm = time.split(":")
            
            hh,mm = int(hh),int(mm)
            if hh > 23:
                return 0
            
            return int(hh * 60 + mm < max_minutes)
        
        N = len(time)
        def backtrack(i,t):
            if i == N:
                #print(t, check(t))
                return check(t)
            ans = 0
            if time[i] == "?":
                if i == 0:
                    for d in range(0,3):
                        ans += backtrack(i+1,t + str(d))
                elif i == 1:
                    for d in range(0,10):
                        ans += backtrack(i+1,t + str(d))
                elif i == 3:
                    for d in range(0,6):
                        ans += backtrack(i+1,t + str(d))
                else:
                    for d in range(0,10):
                        ans += backtrack(i+1,t + str(d))
            else:
                ans += backtrack(i+1,t + time[i])
            return ans
        return backtrack(0,'')
        
        
        