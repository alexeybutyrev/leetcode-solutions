# Problem: Calculate Amount Paid in Taxes
# Language: python3
# Runtime: 83 ms
# Memory: 14 MB

class Solution:
    def calculateTax(self, A: List[List[int]], income: int) -> float:
        A = [[0,0]] + A
        ans = 0
        #print(A)
        for i in range(1,len(A)):
            #print(i,ans, (A[i][0] - A[i-1][0]) * A[i][1]/100)
            if A[i][0] < income:
                ans += (A[i][0] - A[i-1][0]) * A[i][1]/100
            else:
                ans += (income - A[i-1][0]) * A[i][1]/100
                break
                
        return ans