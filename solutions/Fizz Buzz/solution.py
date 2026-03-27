# Problem: Fizz Buzz
# Language: python3
# Runtime: 44 ms
# Memory: 14.7 MB

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(n):
            j = i + 1
            if j % 3 == 0:
                if j % 5 == 0:
                    l.append("FizzBuzz")
                else:
                    l.append("Fizz")
            else:
                if j % 5 == 0:
                    l.append("Buzz")
                else:
                    l.append(str(j))
        return l