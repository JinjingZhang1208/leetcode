class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        # set the key here to be the number, and the value to be the index of the number
        for k, v in enumerate(nums):
            # here the k is the index of nums, v is the value of nums
            diff = target - v
            # diff here would be a key in the hashMap
            if diff in hashMap:
                return [hashMap[diff],k]
            hashMap[v] = k
            # 设置hashMap对比的时候把number放在key，把index 放在value上
            # 和enumerate（nums）时候是反着的
        return []

        # time complexity O(n)
