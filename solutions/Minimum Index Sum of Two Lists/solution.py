# Problem: Minimum Index Sum of Two Lists
# Language: python3
# Runtime: 144 ms
# Memory: 14.9 MB

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        A = {a: i for i,a in enumerate(list1)}
        
        ans = []
        mind = inf
        for j,b in enumerate(list2):
            if b in A and A[b] + j <= mind:
                i = A[b]
                if i + j == mind:
                    ans.append(b)
                else:
                    mind = i+j
                    ans = [b]
        return ans
