# Problem: Sliding Window Maximum
# Language: python3
# Runtime: 1942 ms
# Memory: 43 MB

import math

class SparseTable:
    def __init__(self, data, func):
        """
        :param data: List of integers
        :param func: The idempotent function (min, max, math.gcd, or lambda x, y: x | y)
        """
        self.n = len(data)
        self.func = func
        if self.n == 0: return
        
        self.k = self.n.bit_length()
        # st[j][i] stores the result for range [i, i + 2^j - 1]
        self.st = [[0] * self.n for _ in range(self.k)]
        
        for i in range(self.n):
            self.st[0][i] = data[i]
            
        for j in range(1, self.k):
            for i in range(self.n - (1 << j) + 1):
                self.st[j][i] = self.func(self.st[j-1][i], 
                                          self.st[j-1][i + (1 << (j-1))])

    def query(self, L, R):
        if L > R: return None
        length = R - L + 1
        j = length.bit_length() - 1
        return self.func(self.st[j][L], self.st[j][R - (1 << j) + 1])

class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        N = len(A)

        st = SparseTable(A, max)
        ans = []
        for i in range(N-k+1):
            ans.append(st.query(i,i+k-1))
        return ans