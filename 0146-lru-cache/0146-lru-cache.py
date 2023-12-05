class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # left and right are 2 dummy nodes
        # left points to LRU node, right points to most recent used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    # insert node at the right before the right most
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        # update prev node
        prev.next = node
        node.prev = prev
        # update next node
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove from the list
            self.remove(self.cache[key])
            # insert after the right dummy node
            self.insert(self.cache[key])
            # return
            return self.cache[key].val        
        return -1
        

    def put(self, key: int, value: int) -> None:
        # if the node exists, remove it and insert before the right most
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if it exceeds the cap, remove the LRU
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)