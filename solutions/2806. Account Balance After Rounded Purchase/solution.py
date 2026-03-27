# Problem: Account Balance After Rounded Purchase
# Language: python3
# Runtime: 44 ms
# Memory: 16.4 MB

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - round((purchaseAmount + 0.1) /10) * 10