# Problem: All Divisions With the Highest Score of a Binary Array
# Language: python3
# Runtime: 6360 ms
# Memory: 23.7 MB

class Solution:
    def maxScoreIndices(self, A: List[int]) -> List[int]:
        
        ones = best_score = sum(A)
        zeros = 0
        ans = [0]
        for i,a in enumerate(A):
            if a:
                ones -= 1
                
            else:
                zeros += 1
            
            if ones + zeros == best_score:
                ans.append(i+1)
            elif ones + zeros > best_score:
                best_score = ones + zeros
                ans = [i+1]
        return ans
            
                
            