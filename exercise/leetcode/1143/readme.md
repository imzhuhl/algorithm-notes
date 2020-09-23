需要找到当前状态和之前状态之间的递推关系，用 dp 表示状态数组。

* 例如对于样例 abcde 和 ace 的解，发现两个字符串的最后一个都是 e。因此对于 abcd 和 ac 的最长公共子序列，只要加上 e 就是 abcde 和 ace 的解，即 `dp[i,j] = dp[i-1][j-1]`
* 如果当前状态的两个字符不相同，例如 abcd 和 abdc。发现 abcd 和 abd 的最长子序列是 3，abd 末尾加字符 c 不改变结果。另一方面，abc 和 abdc 的最长子序列是 3，abc 末尾补上 d 不改变结果。因此当前状态取决于 `dp[i-1, j]` 和 `dp[i, j-1]`

综上，判断逻辑如下：

```python
if text1[i-1] == text2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```