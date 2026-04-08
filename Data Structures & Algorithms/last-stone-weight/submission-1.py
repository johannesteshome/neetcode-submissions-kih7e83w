from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            heavy1 = -heappop(stones)
            heavy2 = -heappop(stones)

            left = heavy1 - heavy2

            if left == 0:
                continue
            
            heappush(stones, -left)
        
        if stones:
            return -stones[0]
        return 0