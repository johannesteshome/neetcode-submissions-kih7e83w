class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        N = Total = len(nums)
        
        for i in range(N):
            Total += i - nums[i]
            
        return Total