class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Sum = 0
        Total = 0
        N = len(nums) + 1

        for num in nums:
            Sum += num
        
        for i in range(N):
            Total += i
            
        return Total - Sum