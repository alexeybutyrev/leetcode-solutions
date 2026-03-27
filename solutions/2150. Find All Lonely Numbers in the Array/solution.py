# Problem: Find All Lonely Numbers in the Array
# Language: python3
# Runtime: 2512 ms
# Memory: 38.2 MB

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for k,v in c.items():
            if v == 1 and c[k-1] == c[k+1] == 0:
                ans.append(k)
        return ans