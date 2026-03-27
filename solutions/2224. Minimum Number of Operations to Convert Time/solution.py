# Problem: Minimum Number of Operations to Convert Time
# Language: python3
# Runtime: 51 ms
# Memory: 13.9 MB

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ch, cm = map(int,current.split(":"))
        rh, rm = map(int,correct.split(":"))
        
        tc = ch * 60 + cm
        rc = rh * 60 + rm
        
        if tc < rc:
            tc,rc = rc,tc
            
        ans = 0
        while tc != rc:
            if tc - rc >= 60:
                tc -= 60
            elif tc - rc >= 15:
                tc -= 15
            elif tc - rc >= 5:
                tc -= 5
            else:
                return ans + tc - rc
            ans += 1
            
        return ans
        
        