class Solution:
    def isPalindrome(self, s: str) -> bool:
        newList = []
        for letter in s:
            if letter.isalnum():
                newList.append(letter.lower())
        
        i = 0
        j = len(newList) - 1
        while i < j:
            if newList[i] != newList[j]:
                return False
            i += 1
            j -= 1
        return True
