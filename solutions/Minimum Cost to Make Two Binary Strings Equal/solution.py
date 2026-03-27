# Problem: Minimum Cost to Make Two Binary Strings Equal
# Language: python3
# Runtime: 51 ms
# Memory: 18.1 MB

class Solution:
    def minimumCost(self, s: str, t: str, F: int, swapCost: int, crossCost: int) -> int:
        C = min(swapCost, crossCost)

        z = o = 0
        for x,y in zip(s,t):
            if x != y:
                if x == '0':
                    z += 1
                else:
                    o += 1
        print(o,z)
        ans1 = F * (z+o)
        ans2 = min(o,z) * swapCost + F * abs(z-o)
        ans3 = min(o,z) * swapCost + abs(z - o) // 2 * (swapCost + crossCost) +  abs(z - o) % 2 * F
        return min(ans1, ans2, ans3)

