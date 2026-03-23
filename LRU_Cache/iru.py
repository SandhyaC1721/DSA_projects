class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def insert_front(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert_front(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert_front(node)
        else:
            if len(self.cache) >= self.capacity:
                del self.cache[self.tail.key]
                self.remove(self.tail)

            new_node = Node(key, value)
            self.insert_front(new_node)
            self.cache[key] = new_node

    def print_cache(self):
        temp = self.head
        while temp:
            print(f"({temp.key},{temp.value})", end=" ")
            temp = temp.next
        print()


# Test
cache = LRUCache(3)

cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)
cache.print_cache()

cache.get(1)
cache.print_cache()

cache.put(4, 40)
cache.print_cache()