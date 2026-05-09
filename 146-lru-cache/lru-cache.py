class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}

        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def rem(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev

    def ad(self,node):
        nxt=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=nxt
        nxt.prev=node

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.rem(node)
            self.ad(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.rem(self.cache[key])
        new_node=Node(key,value)
        self.cache[key]=new_node
        self.ad(new_node)

        if len(self.cache)>self.cap:
            lru=self.tail.prev
            self.rem(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)