# Problem: Largest Time for Given Digits
# Language: python3
# Runtime: 40 ms
# Memory: 14.5 MB

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        N = len(arr)
        
        times = []
        def generate(i, used, s):
            if i == N:
                times.append(s)
            else:
                for j,d in enumerate(arr):
                    if j not in used:
                        generate(i+1, used | {j}, s + str(d))
        
        generate(0, set(), "")
        res = []
        for t in times:
            if t[2] in ['0','1','2','3','4','5'] and (t[0] == '2' and t[1] in ['0','2','3','1'] or t[0] in ['0','1']):
                res.append(t)
        if not res:
            return ""
        
        res.sort()
        return res[-1][0:2] + ":" + res[-1][2:4]