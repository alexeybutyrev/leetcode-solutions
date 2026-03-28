# Problem: Defanging an IP Address
# Language: python3
# Runtime: 20 ms
# Memory: 14.1 MB

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")