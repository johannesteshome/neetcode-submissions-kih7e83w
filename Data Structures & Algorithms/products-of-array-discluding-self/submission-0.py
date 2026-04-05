class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixBefore = [1]
        prefixAfter = [1]

        for i in range(len(nums)):
            prefixBefore.append(prefixBefore[-1] * nums[i])
            prefixAfter.append(prefixAfter[-1] * nums[len(nums) - i - 1])
        
        prefixAfter = prefixAfter[::-1]
        
        answer = []
        for i in range(len(nums)):
            answer.append(prefixBefore[i] * prefixAfter[i + 1])
        
        return answer