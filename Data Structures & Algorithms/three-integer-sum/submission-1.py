class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        ptr = 0

        while ptr < len(nums):
            if ptr > 0 and nums[ptr] == nums[ptr - 1]:
                ptr += 1
            else:
                l = ptr + 1
                r = len(nums) - 1

                while l < r:
                    Sum = nums[l] + nums[r]

                    if Sum == -nums[ptr]:
                        res.append([nums[ptr], nums[l], nums[r]])
                        r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif Sum < -nums[ptr]:
                        l += 1
                    else:
                        r -= 1
                
                ptr += 1
        
        return res
