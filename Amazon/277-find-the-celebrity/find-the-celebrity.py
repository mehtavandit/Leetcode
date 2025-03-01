# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # trust_others = [0] * n
        # trusted_by_others = [0] * n

        # for i in range(n):
        #     for j in range(n):
        #         if i!=j:
        #             result = knows(i,j)
        #             if result == True:
        #                 trust_others[i] += 1
        #                 trusted_by_others[j] +=1

        # print(trust_others)
        # print(trusted_by_others)

        # for i in range(n):
        #     if trust_others[i] == 0 and trusted_by_others[i] == n-1:
        #         return i

        # return -1

        #the above approach in O(n2) which will not work

        candidate = 0
        for i in range(1,n):
            if knows(candidate,i): #if candidate know i they can't be the celebrity
                candidate = i #i is now the new candidate

        for i in range(n):
            if i!= candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1 ## Candidate knows someone OR someone doesn't know candidate

        return candidate 

        return 3
