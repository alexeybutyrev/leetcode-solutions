# Problem: Count Covered Buildings
# Language: python3
# Runtime: 407 ms
# Memory: 56 MB

class Solution:
    def countCoveredBuildings(self, n: int, A: List[List[int]]) -> int:
        
        left_most_col = [n+1] * (n+1)
        left_most_row = [n+1] * (n+1)
        right_most_row = [0] * (n+1)
        right_most_col = [0] * (n+1)

        for r,c in A:
            left_most_col[r] = min(left_most_col[r],c)
            left_most_row[c] = min(left_most_row[c],r)


            right_most_row[c] = max(right_most_row[c],r)
            right_most_col[r] = max(right_most_col[r],c)

        ans = 0
        for r,c in A:
            if left_most_col[r] < c < right_most_col[r] and left_most_row[c] < r < right_most_row[c]:
                ans += 1
        return ans