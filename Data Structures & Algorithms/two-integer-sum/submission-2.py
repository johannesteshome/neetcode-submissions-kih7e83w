class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenBefore = defaultdict(int)

        for idx in range(len(nums)):
            num = target - nums[idx]
            if num in seenBefore:
                return [seenBefore[num], idx]
            seenBefore[nums[idx]] = idx
        
        return []