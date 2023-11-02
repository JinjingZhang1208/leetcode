class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        answer = [0] * length
        # index 0 has no element
        answer[0] = 1
        for i in range(1, length):
            # recursion to get the left part total
            answer[i] = nums[i - 1] * answer[i - 1]

        right = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * right
            right *= nums[i]
        
        return answer



        # R[length - 1] = 1
        # for i in range(length - 2, -1, -1):
        #     # another way is to 
        #     # for i in reversed(range(length - 1))
        #     R[i] = nums[i + 1] * R[i + 1]

        # for i in range(length):
        #     answer[i] = L[i] * R[i]
        
        # return answer








            
