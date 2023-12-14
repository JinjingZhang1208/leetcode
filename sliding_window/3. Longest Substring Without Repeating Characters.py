class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        max_count = 0
        sub_string = ""
        
        for char in s:
            if char not in sub_string:
                sub_string += char
                count += 1
            elif char in sub_string:
                sub_string = sub_string[sub_string.index(char) + 1 :] + char
                count = len(sub_string)
            max_count = max(count, max_count)
        
        return max_count