# Problem: Find the K-th Character in String Game II
# Language: python3
# Runtime: 47 ms
# Memory: 16.7 MB

class Solution:
    def kthCharacter(self, k: int, o: List[int]) -> str:
        s = [1]
        for x in o:
            s.append(s[-1] * 2)
        
        c = 0

        for i in range(len(o)-1,-1,-1):
            if k > s[i]:
                k -= s[i]
                if o[i]:
                    c += 1
                    c %= 26
        return chr(c + ord('a'))
