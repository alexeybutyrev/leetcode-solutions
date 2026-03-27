# Problem: Painting a Grid With Three Different Colors
# Language: python3
# Runtime: 2824 ms
# Memory: 14.2 MB

class Solution:
    def colorTheGrid(self, n: int, m: int) -> int:
        MOD = 10**9 + 7
        states = {}
        for state in itertools.product(range(3), repeat = n):
            if all(state[i] != state[i+1] for i in range(n - 1)):
                states[tuple(state)] = 1
        
        mapping = defaultdict(set)
        for s1 in states:
            for s2 in states:
                if all(s1[i] != s2[i] for i in range(n)):
                    mapping[s1].add(s2)
        
        for _ in range(m-1):
            s = Counter()
            for s1 in states:
                for s2 in mapping[s1]:
                    s[s2] += states[s1] % MOD
            states = deepcopy(s)

        return sum(states.values()) % MOD