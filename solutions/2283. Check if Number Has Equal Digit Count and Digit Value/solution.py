# Problem: Check if Number Has Equal Digit Count and Digit Value
# Language: python3
# Runtime: 60 ms
# Memory: 13.8 MB

class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i,x in enumerate(num):
            #print(c,i,x,c[str(i)] == x)
            if c[str(i)] != int(x):
                return False
        return True