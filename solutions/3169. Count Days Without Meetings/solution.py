# Problem: Count Days Without Meetings
# Language: python3
# Runtime: 193 ms
# Memory: 53 MB

def merge(A: List[List[int]]) -> List[List[int]]:
    A.sort()

    B = [A[0]]
    for x,y in A[1:]:
        if x > B[-1][1]:
            B.append([x,y])
        else:
            B[-1][1] = max(y,B[-1][1])
    return B
    
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = merge(meetings)
        A = []
        for a,b in meetings:
            A.append([a,1])
            A.append([b,-1])
        
        A.sort()
        for i in range(1,len(A)):
            A[i][1] += A[i-1][1]
        
        ans = 0
        curr = 1
        seen = True
        for i in range(len(A)):
            if seen:
                ans += A[i][0] - curr
                seen = False
            else:
                if A[i][1] == 0:
                    seen = True
                    curr = A[i][0] + 1

        return ans + days - A[-1][0]
        
        