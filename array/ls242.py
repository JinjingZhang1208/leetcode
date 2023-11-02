class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for letter in t:
        #     if letter in s:
        #         s.remove(letter)
        #         # we could not use remove in string
        #     return False
        # if s is None:
        #     # in Python, to check if a string is empty, you should use if not s, not if s is None. 
        #     return True
        # return False
        # how to count frequency in python :# Iterate through the list and count frequencies
# for item in my_list:
#     # Use get() to increment the count for each item or initialize it to 1 if it doesn't exist
#     frequency_count[item] = frequency_count.get(item, 0)+1
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for letter in s:
            count_s[letter] = count_s.get(letter, 0) + 1
        for letter in t:
            count_t[letter] = count_t.get(letter, 0) + 1
        
        return count_s == count_t
        # when checking if two dictionaries are equal, we can use ==

        # time complexity O(n), space complexity O(n)