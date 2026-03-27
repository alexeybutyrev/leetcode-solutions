# Problem: Letter Combinations of a Phone Number
# Language: python3
# Runtime: 0 ms
# Memory: 17.8 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        ans = [""]

        for x in digits:
            ANS = []
            for s in ans:
                for d in phone_map[x]:
                    ANS.append(s + d)
            ans = ANS[:]
        return ans