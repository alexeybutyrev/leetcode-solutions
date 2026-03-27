# Problem: Grumpy Bookstore Owner
# Language: python3
# Runtime: 325 ms
# Memory: 62.4 MB

class Solution:
    def maxSatisfied(self, A, G, M):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        T = [0]
        for x,g in zip(A,G):
            T.append(T[-1]+x)
        
        N = len(A)
        
        @cache
        def dp(i,j):
            if i>=N: return 0
            s1 = dp(i+1,j) + A[i]*(1-G[i])
            if j: return s1
            return max(s1, dp(i+M, True) + T[min(i+M,len(T)-1)]-T[i])
        
        return dp(0,False)