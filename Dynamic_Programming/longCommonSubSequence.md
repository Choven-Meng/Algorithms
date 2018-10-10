
最大公共子序列（Longest Common Subsequence，LCS）。

其问题是给定两个序列S和T，其长度分别为n和m，求解其最大公共子序列的长度，子序列是指从原序列中任意去掉若干元素（不一定连续）而形成的序列。这个问题的一个应用实例是在基因序列匹配。这里我们假定两个序列都是字符串。比如：S为'abcdfg'，而T为'abdfg'。那么可以得到其LCS为'abdfg'，其长度为5。要使用动态规划来解决这个问题，首先我们要构造递归关系。假定LCS[i,j]为序列S[1..i]和T[1..j]的LCS长度，那么我们是否可以使用更小的实例来求解LCS[i,j]呢？更小的实例是指的是什么？我们不妨将序列减少一个长度，可能的子问题是LCS[i−1][j],LCS[i][j−1],LCS[i−1][j−1]。那么LCS[i][j]是否与这些子问题有关呢？问题的关键是S[i]与T[j]的值，我们分两种情况考虑：

（1）S[i]≠T[j]，此时相当于去掉S[i]或者T[j]，其分别对应于求解LCS[i−1][j]和LCS[i][j−1]，所以LCS[i][j]可以取两者的最大值： 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;LCS[i][j]=max(LCS[i−1][j],LCS[i][j−1])

（2）S[i]=T[j]，此时两个元素匹配，而且它们两个正好匹配一定是最好的结果，假如你想让S[i]匹配T[j]之前的元素，那么S[i]直接匹配T[j]的结果一定不会差于这个结果。所以，最优情况是让两者匹配，那么LCS[i][j]就依赖于LCS[i−1][j−1]： 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;LCS[i][j]=1+LCS[i−1][j−1]

可以看到原问题总是可以利用子问题的解，这正好符合动态规划的原则。我们使用数组LCS[n+1][m+1]保存各个子问题的解，然后采用自下而上的原则，从较小的实例出发，利用递归式不断向前计算，直到求得原问题的解。下面是具体的实现：

```
def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for _ in range(lenb + 1)] for _ in range(lena + 1)]
    flag = [[0 for _ in range(lenb + 1)] for _ in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'
    return c, flag


def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'ok':
        printLcs(flag, a, i - 1, j - 1)
        print(a[i - 1])
    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j - 1)
    else:
        printLcs(flag, a, i - 1, j)


a = 'ABCBDAB'
b = 'BDCABA'
c, flag = lcs(a, b)
for i in c:
    print(i)
print('')
for j in flag:
    print(j)
print('')
printLcs(flag, a, len(a), len(b))
print('')

#output:
[0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 1]
[0, 1, 2, 2, 2, 2]
[0, 1, 2, 2, 2, 2]
[0, 1, 2, 3, 3, 3]
[0, 1, 2, 3, 4, 4]
[0, 1, 2, 3, 4, 5]

[0, 0, 0, 0, 0, 0]
[0, 'ok', 'left', 'left', 'left', 'left']
[0, 'up', 'ok', 'left', 'left', 'left']
[0, 'up', 'up', 'up', 'up', 'up']
[0, 'up', 'up', 'ok', 'left', 'left']
[0, 'up', 'up', 'up', 'ok', 'left']
[0, 'up', 'up', 'up', 'up', 'ok']

abdfg
#第一个矩阵是计算公共子序列长度的，可以看到最长是5；第二个矩阵是构造这个最优解用的；最后输出一个最优解abdfg。
```

```
s1 = [1,3,4,5,6,7,7,8]
s2 = [3,5,7,4,8,6,7,8,2]

d = [[0]*(len(s2)+1) for i in range(len(s1)+1) ]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i-1][j],d[i][j-1])


print ("max LCS number:",d[-1][-1])
#output:max LCS number: 5
```
