class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. count the frequency of each element
        # 2. sort with frequency
        # 3. collect the k top ones

        counted = Counter(nums)

        heap = []

        for key, value in counted.items():
            heap.append((-value, key))
        
        heapq.heapify(heap)

        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])
        
        return answer