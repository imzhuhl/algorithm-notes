

## 回溯

**例题**：[leetcode 416](https://leetcode-cn.com/problems/partition-equal-subset-sum/)

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

> 每个数组中的元素不会超过 100，数组的大小不会超过 200

示例如下：

```
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
```

**思路**：

分成两个子集，元素和相等，等价于从一个数组中不重复的选取一些元素，使得这些元素的和为数组总和的一半。本题可以使用动态规划，也可以使用回溯法，动态规划的思路见[动态规划 01背包问题](../dynamic_programming/readme.md#01背包)。因为只需要有一个解成立即可返回，所以不需要考虑其他可能，因此用回溯法非常高效。回溯的基本写法如下：

```python
def canPartition(self, nums: List[int]) -> bool:
    nums.sort()
    s = sum(nums)
    if s % 2 != 0:
        return False
    target = s // 2
    return self.dfs(0, target, nums)

def dfs(self, cur: int, rest: int, nums: List[int]):
	if rest == 0:
        return True
    if rest < 0:
        return False
    for i in range(cur, len(nums)):
        ret = self.dfs(i+1, rest-nums[i], nums)
        if ret:
            return True
	return False    
```

测试样例会可能出现极端情况，例如 `[1, 1, 1, ..., 1000]` ，这种情况下回溯法很容易超时，因此我们需要及时剪枝，例如当前这一步和上一步是相同的值时，就可以直接剪枝，因为相同的输入，会导致相同的输出：

```
考虑第三个节点:
{1, 1} -> 1(第三个1) -> ...
{1, 1} -> 1(第四个1)  # 与之前的值相同，剪枝，不用考虑后面了
```

只需要增加如下代码：

```python
# ...
for i in range(cur, len(nums)):
    if i > cur and nums[i] == nums[i-1]:  # 剪枝
        continue
    ret = self.dfs(i+1, rest-nums[i], nums)
    if ret:
        return True
# ...
```

另外，由于我们是从小到大排序，如果当前元素已经大于 rest，就不用考虑之后的元素了，因为一定都大于 rest，直接 break 循环也可以节省不少时间，dfs 函数可以修改如下。

```python
def dfs(self, cur: int, rest: int, nums: List[int]):
    for i in range(cur, len(nums)):
        if i > cur and nums[i] == nums[i-1]:
        	continue
        if nums[i] > rest:  # 当前元素大于 rest, 就不用考虑之后的元素了, 直接结束循环
            break
        if nums[i] == rest:
            return True
        ret = self.dfs(i+1, rest-nums[i], nums)
        if ret:
            return True
	return False 
```

**代码**：[416](./backtracking/0416.py)