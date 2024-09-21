# LRU Cache
# Fixed size, positive capacity.
# We want O(1) time operations.

class Node: 
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None 
        self.next = None

class LRUCache:

    # constructor.
    def __init__(self, capacity: int):
       
        # we'll likely decrement as we add.
        self.capacity = capacity

        self.cache = {} # <Key, Nodes> 

        self.left = Node(0, 0) # least recent used
        self.right = Node(0, 0) # most recent used

        # nodes need to be connected. 
        self.left.next = self.right
        self.right.prev = self.left

    # NOTE: return value of the key if it exists,
    # if not, return -1
    # NOTE: also every time we get a value, we want to 
    # update it to most recent.
    def get(self, key: int) -> int:
        if key in self.cache: 
            # remove first. 
            self.remove(self.cache[key])
            
            # add to right side, since most 
            # recently used.
            self.insertRight(self.cache[key])

            return self.cache[key].val # returns node.
        return -1

    # helper function
    def remove(self, node):
        prevNode, nxtNode = node.prev, node.next
        prevNode.next = nxtNode
        nxtNode.prev = prevNode

    # helper function
    def insertRight(self, node): 
        prevNode = self.right.prev
        rightMostNode = self.right
        prevNode.next = node
        rightMostNode.prev = node
        node.next = rightMostNode
        node.prev = prevNode

    # update the value of the key if the key exists,
    # otherwise, add the key-value pair to the cache.
    # if the number of keys exceeds the capacity from 
    # this operation, evict the LEAST RECENTLY USED
    # key from the cache.
    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insertRight(self.cache[key])

        if len(self.cache) > self.capacity:
            # uh oh. we need to evict. 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]


        