
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prv = None
        self.nxt = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.end = Node(0, 0)
        self.head.nxt = self.end
        self.end.prv = self.head
        self.table = {}

    def get(self, key: int) -> int:
        if key in self.table:
            value = self.table[key].val
            self.move_to_head(self.table[key])
            return value
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        if key not in self.table:
            if len(self.table) >= self.capacity:
                tg_node = self.end.prv
                del self.table[tg_node.key]
                tg_node.key = key
                tg_node.val = value
                self.table[key] = tg_node
                self.move_to_head(tg_node)
            else:
                tg_node = Node(key, value)
                self.insert_to_head(tg_node)
                self.table[key] = tg_node
        else:
            tg_node = self.table[key]
            tg_node.val = value
            self.move_to_head(tg_node)

    def insert_to_head(self, node):
        t = self.head.nxt
        self.head.nxt = node
        node.prv = self.head
        node.nxt = t
        t.prv = node    
        
    def move_to_head(self, node):
        pre_node = node.prv
        nxt_node = node.nxt
        
        # remove node in linklist
        pre_node.nxt = nxt_node
        nxt_node.prv = pre_node
        
        # insert to head
        self.insert_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)