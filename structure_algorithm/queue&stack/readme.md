## queue

#### python 实现

python 中有两种办法实现 queue，分别是使用 list 和 collections.deque

list 是数组，deque 是使用双向链表实现的

```python
queue = []
queue.append(x)  # 入队列
queue.pop(0)  # 出队列, O(n)

queue = collections.deque()
queue.append(x)
queue.popleft()  # O(1)
```

