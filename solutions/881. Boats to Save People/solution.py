# Problem: Boats to Save People
# Language: python3
# Runtime: 354 ms
# Memory: 23.6 MB

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        A = deque(people)
        ans = 0
        while A:
            if len(A) == 1:
                ans += 1
                A.pop()
                continue
                
            if A[-1] + A[0] <= limit:
                A.popleft()
                A.pop()
                ans +=1
            else:
                A.pop()
                ans += 1
        return ans