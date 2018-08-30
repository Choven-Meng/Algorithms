### 1. 每种元素个数(每种面值的纸币)无限

**题目：**

  假设我们有8种不同面值的硬币｛1，2，5，10，20，50，100，200｝，用这些硬币组合够成一个给定的数值n。例如n=200，那么一种可能的组合方式为    
200 = 3 * 1 + 1＊2 + 1＊5 + 2＊20 + 1 * 50 + 1 * 100. 问总过有多少种可能的组合方式？

**解题思路：**

  这道题目是非常经典的动态规划算法题。给定一个数值sum，假设我们有m种不同类型的硬币v1,v2,...,vm，如果要组合成sum，那么我们有   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sum = x1∗v1 + x2∗v2 + ...+ xm∗vm   

求所有可能的组合数，就是求满足前面等值的系数x1,x2,...,xm的所有可能个数。  

  从上面的分析中我们也可以这么考虑，我们希望用m种硬币构成sum，根据最后一个硬币Vm的系数的取值为无非有这么几种情况，x<sub>m</sub>分别取｛0, 1, 2, ..., sum/V<sub>m</sub>｝，换句话说，上面分析中的等式和下面的几个等式的联合是等价的。

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sum = x1 * V1 + x2 * V2 + ... + 0 * Vm

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sum = x1 * V1 + x2 * V2 + ... + 1 * Vm

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sum = x1 * V1 + x2 * V2 + ... + 2 * Vm

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;...

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sum = x1 * V1 + x2 * V2 + ... + K * Vm  
　　
  其中K是该xm能取的最大数值K = sum / Vm。可是这又有什么用呢？不要急，我们先进行如下变量的定义：

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dp[i][sum] = 用前i种硬币构成sum 的所有组合数。
　
 
  那么题目的问题实际上就是求dp[m][sum]，即用前m种硬币（所有硬币）构成sum的所有组合数。在上面的联合等式中：当x<sub>n</sub>=0时，有多少种组合呢？ 实际上就是前i-1种硬币组合sum，有dp[i-1][sum]种！ x<sub>n</sub> = 1 时呢，有多少种组合？ 实际上是用前i-1种硬币组合成(sum - V<sub>m</sub>)的组合数，有dp[i-1][sum -Vm]种; x<sub>n</sub> =2呢， dp[i-1][sum - 2 * Vm]种，等等。所有的这些情况加起来就是我们的dp[i][sum]。所以：

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dp[i][sum] = dp[i-1][sum - 0*Vm] + dp[i-1][sum - 1*Vm]+ dp[i-1][sum - 2*Vm] + ... + dp[i-1][sum - K*Vm]; 其中K = sum / Vm

换一种更抽象的数学描述就是：  

&emsp;&emsp;&emsp;&emsp;&emsp;<a href="https://www.codecogs.com/eqnedit.php?latex=dp[i][sum]&space;=&space;\sum_{k=0}^{sum/V_{m}}dp[i-1][sum-k*V_{m}]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?dp[i][sum]&space;=&space;\sum_{k=0}^{sum/V_{m}}dp[i-1][sum-k*V_{m}]" title="dp[i][sum] = \sum_{k=0}^{sum/V_{m}}dp[i-1][sum-k*V_{m}]" /></a>

  通过此公式，我们可以看到问题被一步步缩小，那么初始情况是什么呢？如果sum=0，那么无论有前多少种来组合0，只有一种可能，就是各个系数都等于0；

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dp[i][0] = 1   // i = 0, 1, 2, ... , m

  如果我们用二位数组表示dp[i][sum], 我们发现第i行的值全部依赖与i-1行的值，所以我们可以逐行求解该数组。如果前0种硬币要组成sum，我们规定为dp[0][sum] = 0. 

**动态规划：**  

1、构成N的组合数
```
def getNumberOfCombinations(coins,N):
    coinKinds = len(coins)
    dp = [[0 for _ in range(N+1)] for _ in range(coinKinds+1)]
    
    # 初始化dp，因为当总和N为0时，只有一种情况即coins元素系数都为0
    for i in range(coinKinds):
        dp[i][0] = 1 #前i种纸币组合成0，只有一种情况就是个数均为0
    for i in range(1,coinKinds+1):
        for j in range(1,N+1):
            dp[i][j] = 0
            for k in range(int(j/coins[i-1] + 1)):  #coins中每个元素的系数
                dp[i][j] += dp[i-1][j-k*coins[i-1]]
    return dp
    
if __name__ == '__main__':
    coins = [1,2,5,10,20,50,100,200]
    N = 200
    getNumberOfCombinations(coins,N)
#output:73682
```

2、构成N的最小组合数
```
def getLeastNumberOfCombinations(coins,N):
    coinKinds = len(coins)
    dp = [[float('inf') for _ in range(N+1)] for _ in range(coinKinds+1)]
    
    for i in range(coinKinds+1):
        dp[i][0] = 0  # 当N为0时，所有系数都为0
    for i in range(1,coinKinds+1):
        for j in range(1,N+1):
            for k in range(int(j/coins[i-1] + 1)):  #coins中每个元素的系数
                if dp[i-1][j-k*coins[i-1]] + k < dp[i][j]:
                    dp[i][j] = dp[i-1][j-k*coins[i-1]] + k
    return dp[coinKinds][N]
    
if __name__ == '__main__':
    coins = [1,2,5,10,20,50,100,200]
    N = 200
    getNumberOfCombinations(coins,N)
#output:1
```


### 2. 每种元素个数有限

