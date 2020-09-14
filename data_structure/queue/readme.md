## 队列 queue

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



## 单调队列

单调队列指的是保持队列内元素有序（递增或者递减）的队列

**例题**：

[leetcode 239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。返回滑动窗口中的最大值。

示例

```
输入: nums = [1,3,-1,-3,5,3,6,7], k = 3
输出: [3,3,5,5,6,7]

滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**思路**：

此题可以维护一个递减的单调队列，队首元素就是最大值。

问题在于如何维护一个递减的队列，使用到双向队列，针对上述例子：

```
[1 3 -1] -3 5 3 6 7       [3, -1]
1 [3 -1 -3] 5 3 6 7				[3, -1, -3]
1 3 [-1 -3 5] 3 6 7				[5]
...
```

首先，队列必须是递减的，例如一开始 1 入队列，但是下一个入队的 3 大于 1，因此 1 必须出队列。因为 1 首先入队列，并且比 3 要小，可以认为在之后的过程中，只要 3 一直在滑动窗口内，最大值就不可能是 1，因此可以将 1 出队列。

**代码**： [0239](./0239.py)