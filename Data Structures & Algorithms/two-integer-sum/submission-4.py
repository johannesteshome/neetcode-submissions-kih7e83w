class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedList = []

        for i in range(len(nums)):
            sortedList.append((nums[i], i))
        
        sortedList.sort()

        i = 0
        j = len(sortedList) - 1

        while i < j:
            Sum = sortedList[i][0] + sortedList[j][0]
            if Sum > target:
                j -= 1
            elif Sum < target:
                i += 1
            else:
                return [min(sortedList[i][1], sortedList[j][1]), max(sortedList[i][1], sortedList[j][1])]