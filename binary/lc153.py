class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Check if the minimum is in the left or right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
