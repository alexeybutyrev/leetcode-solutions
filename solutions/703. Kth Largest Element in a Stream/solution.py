# Problem: Kth Largest Element in a Stream
# Language: python3
# Runtime: 76 ms
# Memory: 20.4 MB

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.K = k
        for x in nums:
            heappush(self.h, x)
            if len(self.h) > k:
                heappop(self.h)

    def add(self, val: int) -> int:
        heappush(self.h, val)
        if len(self.h) > self.K:
            heappop(self.h)
        ans = heappop(self.h)
        heappush(self.h, ans)
        return ans


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)