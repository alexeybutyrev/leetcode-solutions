# Problem: Lexicographically Smallest String After Deleting Duplicate Characters
# Language: python3
# Runtime: 1394 ms
# Memory: 21.5 MB

from string import ascii_lowercase
class Solution:
    def lexSmallestAfterDeletion(self, S: str) -> str:
        c = Counter()
        for i,x in enumerate(S):
            c[ord(x) - ord('a')] += 1
        
        used = [0] * 26
        s = []
        for x in S:
            i = ord(x) - ord('a')
            c[i] -= 1
            while s and s[-1] > x:
                top = ord(s[-1]) - ord('a')
                if used[top] + c[top] > 1:
                    used[top] -=1
                    s.pop()
                    
                else:
                    break
            


            s.append(x)
            used[i] += 1
            

        while s:
            i = ord(s[-1]) - ord('a')
            if used[i] > 1:
                s.pop()
                used[i] -= 1
            else:
                break
        
                
        return "".join(s)