class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1  
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def pop_tail(self):
        if self.head.next == self.tail:  
            return None
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.node_map = {}  # Maps key to node
        self.freq_map = {}  # Maps freq to DoublyLinkedList
        self.min_freq = 0  

    def update_frequency(self, node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        if not self.freq_map[freq].head.next != self.freq_map[freq].tail:
            del self.freq_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        node.freq += 1
        freq = node.freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoublyLinkedList()
        self.freq_map[freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.update_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self.update_frequency(node)
        else:
            if self.size >= self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                node_to_evict = lfu_list.pop_tail()
                del self.node_map[node_to_evict.key]
                self.size -= 1

            new_node = Node(key, value)
            self.node_map[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].add_node(new_node)
            self.min_freq = 1
            self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)