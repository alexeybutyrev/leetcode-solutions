# Problem: Total Distance Traveled
# Language: python3
# Runtime: 94 ms
# Memory: 16.4 MB

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank:
            if mainTank >=5:
                ans += 50
                mainTank -= 5
                if additionalTank:
                    additionalTank -= 1
                    mainTank += 1
            else:
                ans += mainTank * 10
                mainTank = 0
        return ans