class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        counter = 0


        while (left <= right):
            
            if (left != right):
                sum_ = people[left] + people[right]

                if (sum_ <= limit):
                    counter += 1
                    left += 1
                    right -= 1
                else:
                    counter += 1
                    right -= 1

            else:
                if (people[left] <= limit):
                    counter += 1
                    left += 1
                    right -= 1


        return counter