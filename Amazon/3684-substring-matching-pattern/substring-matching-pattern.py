class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        left_part, right_part = p.split('*')

        left_idx = s.find(left_part)
        right_idx = s.find(right_part, left_idx + len(left_part))

        return left_idx != -1 and right_idx != -1
