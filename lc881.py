class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        sorted_people = sorted(people)
        boats = 0
        i = 0
        j = len(sorted_people) - 1
        
        while i <= j:
            if sorted_people[i] + sorted_people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        
        return boats