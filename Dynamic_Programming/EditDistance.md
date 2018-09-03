编辑距离

# 问题描述

给定 2 个字符串 a, b. 编辑距离是将 a 转换为 b 的最少操作次数，操作只允许如下 3 种：

插入一个字符，例如：fj -> fxj
删除一个字符，例如：fxj -> fj
替换一个字符，例如：jxj -> fyj

# 思路
（https://www.cnblogs.com/sheeva/p/6598449.html）

用分治的思想解决比较简单，将复杂的问题分解成相似的子问题。

假设字符串 a, 共 m 位，从 a[1] 到 a[m]  
字符串 b, 共 n 位，从 b[1] 到 b[n]  
d[i][j] 表示字符串 a[1]-a[i] 转换为 b[1]-b[j] 的编辑距离。

那么有如下递归规律（a[i] 和 b[j] 分别是当前要计算编辑距离的子字符串 a 和 b 的最后一位）：

1、当 a[i] 等于 b[j] 时，d[i][j] = d[i-1][j-1], 比如 fxy -> fay 的编辑距离等于 fx -> fa 的编辑距离

2、当 a[i] 不等于 b[j] 时，d[i][j] 等于如下 3 项的最小值：
    
    1.d[i-1][j] + 1（删除 a[i]（删除等价于插入操作，相当于插入b中插入a[i]）），比如 fxy -> fab 的编辑距离 = fx -> fab 的编辑距离 + 1
    
    2.d[i][j-1] + 1（删除 b[j]或者插入b[j])，比如 fxy -> fab 的编辑距离 = fxyb -> fab 的编辑距离 + 1 = fxy -> fa 的编辑距离 + 1
    
    3.d[i-1][j-1] + 1（将a[i]b[j]同时删除（等价于交换操作）），比如 fxy -> fab 的编辑距离 = fxb -> fab 的编辑距离 + 1 = fx -> fa 的编辑距离 + 1
    
递归边界：

1、a[i][0] = i, b 字符串为空，表示将 a[1]-a[i] 全部删除，所以编辑距离为 i

2、a[0][j] = j, a 字符串为空，表示 a 插入 b[1]-b[j]，所以编辑距离为j

```
def minDistance( word1, word2):
    m = len(word1) + 1
    n = len(word2) + 1

    dp = []
    # (m+1)*（n+1）二维矩阵
    dp = [[0 for i in range(n)] for j in range(m)]  

    for i in range(n):
        dp[0][i] = i

    for i in range(m):
        dp[i][0] = i

    for i in range(1, m):

        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1))

    return dp[m - 1][n - 1]
```
