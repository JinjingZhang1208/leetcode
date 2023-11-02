class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = {}
        # create a dicitonary
        for s in strs:
            sorted_str = "".join(sorted(s))
            # create a unique key
            # check if the key is in the dictionary ans
            if sorted_str not in ans:
                # 先要check不在
                ans[sorted_str] = [s]
            else:
                ans[sorted_str].append(s)
        
        return list(ans.values())

# You iterate through each string in strs, which gives you O(n) as the outer loop.
# For each string, you sort its characters using the sorted function. 
# Sorting a string of length k takes O(k * log(k)) time complexity.
# Since you perform the sorting operation for each string in strs, 
# the overall time complexity becomes 
# O(n * k * log(k)).


# better way to improve:
# ans = defaultdict(list)
# for s in strs:
#     sorted_str = "".join(sorted(s))
#     ans[sorted_str].append(s)
