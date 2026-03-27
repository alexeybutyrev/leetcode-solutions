# Problem: Maximize the Confusion of an Exam
# Language: python3
# Runtime: 427 ms
# Memory: 14.5 MB

from itertools import groupby
class Solution:
    def maxConsecutiveAnswers(self, S: str, k: int) -> int:
        ans = l = t = f = 0
        
        for i in range(len(S)):
            if S[i] == "T":
                t += 1
            else:
                f += 1
            
            
            while min(t,f) > k:
                if S[l] == "T":
                    t -= 1
                else:
                    f -= 1
                l+=1
                
            ans = max(i - l + 1, ans)
        
        return ans