# Problem: Largest Number After Mutating Substring
# Language: python3
# Runtime: 263 ms
# Memory: 15.8 MB

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
   
        ans = ""
        N = len(num)
        for i,l in enumerate(num):
            n = int(l)
            if change[n] > n:
                while i < N and change[n] >= n:
                    ans += str(change[n])
                    i+=1
                    if i < N:
                        n = int(num[i])
                return ans + num[i:]
            else:
                ans += l
        
        
                
        return ans
            