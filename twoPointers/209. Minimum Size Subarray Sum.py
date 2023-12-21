class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        minCount = float('inf')
        total = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                minCount = min(minCount, right - left + 1)
                total -= nums[left]
                left += 1
        
        if minCount == float('inf'):
            return 0
        return minCount
                