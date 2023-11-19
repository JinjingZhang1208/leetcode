class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element
                # 如果新一个index i 和之前一个index i是同一个value，那就要不loop这个了。因为set must not contain duplicate triplets.
                # The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration. 
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left +=1

                    # skip duplicate for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif currentSum < 0:
                    left += 1
                
                else:
                    right -= 1
        
        return result
