# Problem: Find The Least Frequent Digit
# Language: python3
# Runtime: 2 ms
# Memory: 17.8 MB

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        c = Counter(str(n))
        A = [(x,y) for y,x in c.items()]
        A.sort()
        return int(A[0][1])