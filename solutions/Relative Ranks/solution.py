# Problem: Relative Ranks
# Language: python3
# Runtime: 78 ms
# Memory: 18.1 MB

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        A = [[str(c),c,i] for i,c in enumerate(score)]
        A.sort(key=lambda x:-x[1])
        A[0][0]= "Gold Medal"
        if len(A)>1:
            A[1][0]= "Silver Medal"
        if len(A)>2:
            A[2][0]= "Bronze Medal"
        for j in range(3,len(A)):
            A[j][0]=str(j+1)
        A.sort(key= lambda x: x[2])
        
        return [x for x,_,_ in A]