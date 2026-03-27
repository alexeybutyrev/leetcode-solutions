# Problem: Minimum Pair Removal to Sort Array II
# Language: python3
# Runtime: 4960 ms
# Memory: 74.9 MB

class Node:
    def __init__(self,value,left):
        self.value = value
        self.left = left
        self.prev = None
        self.next = None

class PQ:
    def __init__(self, first, second, cost):
        self.first = first
        self.second = second
        self.cost = cost

    def __lt__(self, other):
        if self.cost == other.cost:
            return self.first.left < other.first.left
        return self.cost < other.cost

class Solution:
    def minimumPairRemoval(self, A: List[int]) -> int:
        pq = []
        head = Node(A[0], 0 )
        N = len(A)
        curr = head
        merged = [False] * N

        decrease_count = count = 0

        for i in range(1, N):
            nn = Node(A[i],i)
            curr.next = nn
            nn.prev = curr

            heappush(pq, PQ(curr, nn, curr.value + nn.value))

            if A[i-1] > A[i]:
                decrease_count += 1
            curr = nn
        
        while decrease_count:
            item = heappop(pq)
            first, second, cost = item.first, item.second, item.cost

            if merged[first.left] or merged[second.left] or first.value + second.value != cost:
               continue
            count += 1

            if first.value > second.value:
                decrease_count -=1
            
            prev_node = first.prev
            next_node = second.next
            first.next = next_node

            if next_node:
                next_node.prev = first

            if prev_node:
                if prev_node.value > first.value and prev_node.value <= cost:
                    decrease_count -= 1
                elif prev_node.value <= first.value and prev_node.value > cost:
                    decrease_count += 1
                
                heappush(pq, PQ(prev_node, first, prev_node.value + cost))
            

            if next_node:
                if second.value > next_node.value and cost <= next_node.value:
                    decrease_count -= 1
                elif second.value <= next_node.value and cost > next_node.value:
                    decrease_count += 1
                
                heappush(pq, PQ(first, next_node,  next_node.value + cost))
            first.value = cost
            merged[second.left] = True
        
        return count
            
