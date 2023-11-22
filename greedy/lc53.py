class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize to negative infinity to handle an array of all negative numbers
        # maxSum = float('-inf')
        # #  or maxSum = nums[0]
        # currentSum = 0
        # for i in range(len(nums)):
        #     currentSum = max(nums[i], currentSum + nums[i])
        #     maxSum = max(maxSum, currentSum)

        # return maxSum

        maxSum = nums[0]
        # maxSum could be negative, so could not set to be 0
        currentSum = 0
        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maxSum = max(maxSum, currentSum)
        return maxSum
                
