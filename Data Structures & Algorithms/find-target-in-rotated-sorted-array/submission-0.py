class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binarySearch(arr):

            left, right = 0, len(arr) - 1

            while left < right:

                mid = left + (right - left) // 2

                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        def binarySearchTarget(arr, target):
            left, right = 0, len(arr) - 1

            while left <= right:

                mid = left + (right - left) // 2

                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1

        pivot = binarySearch(nums)

        print(pivot)

        if target <= nums[-1]:
            res = binarySearchTarget(nums[pivot:], target)

            if res != -1:
                return pivot + res
            return -1
        else:
            return binarySearchTarget(nums[:pivot], target)
        
        