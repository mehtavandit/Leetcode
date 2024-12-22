class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l1 = len(s)
        l2 = len(goal)

        if (l1 != l2):
            return False

        new_string = s + s

        if goal in new_string:
            return True
        else:
            return False