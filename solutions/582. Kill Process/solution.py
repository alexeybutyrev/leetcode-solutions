# Problem: Kill Process
# Language: python3
# Runtime: 452 ms
# Memory: 27.1 MB

from collections import defaultdict
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], k: int) -> List[int]:
        ans = []
        seen = {k}
        hm = defaultdict(set)
        for ind, n in enumerate(ppid):
            hm[n].add(pid[ind])

        def kill(i):
            ans.append(i)
            if i in hm:
                for p in hm[i]:
                    if p not in seen:
                        seen.add(p)
                        kill(p)
        kill(k)
        return ans