from collections import defaultdict

class LockingTree:

    def __init__(self, parent: List[int]):
        self.locks = [0] * len(parent) #status of locks
        self.parent = parent #parents of all nodes
        self.children = defaultdict(list) #for a particular node to store its childrens

        for i,p in enumerate(parent): #i is index, p is parent, so will give children access
            if p!=-1:
                self.children[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] != 0:
            return False
        self.locks[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] != user:
            return False
        self.locks[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locks[num] != 0:
            return False
        
        if not self.check_lock_descendants(num): #check there exists any one locked descendant
            return False

        if self.check_lock_ancestors(num):
            return False

        self.lock(num, user)
        self.unlock_descendants(num)
        return True


    def check_lock_descendants(self, num):
        stack = [n for n in self.children[num]] # add childrens of num to stack

        while stack:
            element = stack.pop()
            if self.locks[element] != 0:
                return True
            stack.extend(self.children[element])
        
        return False

    def check_lock_ancestors(self, num):
        while num != -1:
            if self.locks[num] != 0:
                return True
            num = self.parent[num]
        return False

    def unlock_descendants(self, nums):
        stack = [n for n in self.children[nums]]

        while stack:
            element = stack.pop()
            self.locks[element] = 0
            stack.extend(self.children[element])
# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)