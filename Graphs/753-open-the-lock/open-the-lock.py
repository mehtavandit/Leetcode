from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadset = set(deadends)


        if target in deadset:
            return -1

        if "0000" in deadset:
            return -1
        
        q = deque()
        q.append(("0000",0))
        visited = set('0000')

        while q:
            current_value, moves = q.popleft()

            if current_value == target:
                return moves
            
            for i in range(4):
                for deviation in [-1,1]:
                    new_digit = (int(current_value[i])+deviation)%10
                    new_value = current_value[:i] + str(new_digit) + current_value[i+1:]

                    if new_value not in visited and new_value not in deadset:
                        visited.add(new_value)
                        q.append((new_value, moves+1))

        return -1


            