class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. count the frequency of each element
        # 2. sort with frequency
        # 3. collect the k top ones

        counted = Counter(nums)

        heap = []
        for key, value in counted.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        answer = []
        for freq, item in heap:
            answer.append(item)
        
        return answer