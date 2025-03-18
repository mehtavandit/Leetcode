class Solution:
    def isPathCrossing(self, path: str) -> bool:
        start = [0,0]
        visited = set()
        visited.add(tuple(start))

        for i in path:
            if i == "N":
                start[1] += 1
            elif i == "S":
                start[1] -= 1
            elif i == "E":
                start[0] += 1
            elif i == "W":
                start[0] -= 1

            print(start)
            
            if tuple(start) in visited:
                return True
            
            visited.add(tuple(start))

        return False
            
            