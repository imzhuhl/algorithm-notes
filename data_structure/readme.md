# 树 Tree

二叉树，平衡二叉树（AVL），红黑树



# 堆 Heap





# 并查集 **disjoint-set**

也称 union–find data structure，并查集是一种树形结构，适合处理不交集的**合并**和**查询**。

并查集包含两种操作 find 和 union，find 表示查找某一个元素属于哪个集合，union 表示合并两个集合。之后的内容如下：

* 并查集的实际操作
* 例题
* 优化

#### 实际操作

首先设置一个 father 数组，表示每一个元素所属的类别，一开始的时候每一个元素自成一类：

```python
# father 数组 fa 初始化
for i in range(n):
    fa[i] = i
```

定义操作 find：

```python
def find(x):
    if fa[x] != x:
        return find(fa[x])
   	else:
        return x
```

find 操作的逻辑是查找元素 x 所属的集合，然后返回这个集合中的一个代表元素，如果 `fa[x]==x` 表示 x 就是这个集合的代表元素，就立即返回，如果不是，则通过 father 数组网上寻找，找到代表元素。

定义 union 操作：

```python
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:  # 本身就属于一个集合
        return
   	fa[x] = y	# 合并集合，x 的上级元素是 y
```

合并操作会将 x 所属的集合和 y 所属的集合合并在一起。

#### 例题

[leetcode 547](https://leetcode-cn.com/problems/friend-circles/)

班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果 `M[i][j]=1`，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

```
输入：
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出：1
解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。
```

**思路**：

首先初始化 father 数组，并写好 find 和 union。接着开始统计遍历数组，合并小朋友的朋友圈：

```python
for i in range(len(M)):
    for j in range(i+1, len(M)):
        if M[i][j] == 1:
            union(i, j)
```

这个步骤后，同一个朋友圈的小朋友 i 会有相同的 find(i)。接着判断有多少个朋友圈：

```python
cnt = 0
for i in range(len(M)):
    if fa[i] == i:
        cnt += 1
```

`cnt` 就是朋友圈的数量，直接用 `fa[i] == i` 就可以判定这是不是一个集合的代表元素，有多少个代表元素就有多少个集合。

**代码**：[547](./disjoint/0547.py)























