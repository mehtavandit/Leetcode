class FileSystem:

    def __init__(self):
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        
        if path == "/" or len(path) == 0 or path in self.paths:
            return False

        parent = path[:path.rfind('/')]
        
        if len(parent) > 1 and parent not in self.paths:
            return False

        self.paths[path] = value
        return True



    def get(self, path: str) -> int:
        retrived_path = self.paths[path] if path in self.paths else -1

        return retrived_path 


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)