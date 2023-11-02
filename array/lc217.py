class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
            # if not nums:
            #     return False
            # res = []
            # for i in nums:
            #     if i not in res:
            #         res.append(i)
            #     else:
            #         return True
            # return False
            # Wrong ---- time limit exceeded
            hashSet = set()
            for i in nums:
                if i not in hashSet:
                    hashSet.add(i) 
                else:
                    return True
            return False
            # sets have O(1) average time complexity for membership tests whereas lists have O(n) time complexity for such operations.
            # use .add() for set
