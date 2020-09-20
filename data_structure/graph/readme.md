# 例题

| 题目                                                         | 题解                      | 思路                 |
| ------------------------------------------------------------ | ------------------------- | -------------------- |
| [leetcode 207 课程表](https://leetcode-cn.com/problems/course-schedule/) | [py3](./exercise/0207.py) | 判断是否为有向无环图 |
|                                                              |                           |                      |
|                                                              |                           |                      |



# 有向无环图

Directed Acyclic Graph，缩写 DAG，边有向，无环

如何判定一个图是有向无环图：

* DFS，看看是否会遍历到先前遍历过的节点
* 能否进行拓扑排序

有向无环图和树的区别：[链接](https://blog.csdn.net/XXJ19950917/article/details/78046550)

关于有向无环图的判断见例题 [leetcode 207 课程表](https://leetcode-cn.com/problems/course-schedule/)。

# 拓扑排序

拓扑排序针对有向无环图。我们将图中的顶点以线性方式进行排序，使得排在前面的节点不能依赖于排在后面的节点。

## Kahn 算法

将入度为 0 的点组成一个集合 $ S $，每次从 $ S $ 中取出一个点 $u$ 放入 $L$，然后遍历顶点 $u$ 的所有边并删除，并判断如果该边的另一个顶点此时的入度为 0，则加入 $S$，不断重复此操作直到 $S$ 中没有点为止。

### 伪代码

```
L <- 空数组, 将会存储拓扑的结果;
S <- 入度为 0 的节点集合;
while S is not empty {
    n <- 从 S 中选一个节点;
    将 n 加入数组 L;
    for 顶点是 n 的边 {
        v <- 边上的另一个节点;
        删除边;
        if v 的入度是 0 {
            v 加入 S;
        }
    }
}
if 图还存在其他边 {
    return error; (无法进行拓扑排序)
} else {
    return L; 
}
```

## DFS 算法

参考 [leetcode 207 课程表](https://leetcode-cn.com/problems/course-schedule/)，只需要加入栈，将已经 check 的点依次放入栈中，最后依次出栈，出栈顺序就是拓扑排序的顺序。



# 最短路径







