class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        for i in nums:
            ans[i] = ans.get(i, 0) + 1
        # sort the dictionary in descending order
        sorted_ans = sorted(ans.items(), key=lambda x:x[1], reverse = True)
        top_K = [item[0] for item in sorted_ans[:k]]
        return top_K

# time complexity: O(n log n) 
# space complexity: O(n) 

