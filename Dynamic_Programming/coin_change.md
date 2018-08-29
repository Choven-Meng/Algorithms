假设我们有8种不同面值的硬币｛1，2，5，10，20，50，100，200｝，用这些硬币组合够成一个给定的数值n。例如n=200，那么一种可能的组合方式为    
200 = 3 * 1 + 1＊2 + 1＊5 + 2＊20 + 1 * 50 + 1 * 100. 问总过有多少种可能的组合方式？

这道题目是非常经典的动态规划算法题。给定一个数值sum，假设我们有m种不同类型的硬币v1,v2,...,vm，如果要组合成sum，那么我们有 sum=x1∗v1+x2∗v2+...+xm∗vm
求所有可能的组合数，就是求满足前面等值的系数x1,x2,...,xm的所有可能个数。  

定义dp[i][sum] = 用前i种硬币构成sum 的所有组合数。   
那么题目的问题实际上就是求dp[m][sum]，即用前m种硬币（所有硬币）构成sum的所有组合数。    
在上面的联合等式中，当xm=0时，有多少种组合呢？ 实际上就是前i-1种硬币组合sum，有dp[i-1][sum]种！    
xm=1时呢，有多少种组合？ 实际上是用前i-1种硬币组合成(sum - Vm)的组合数，有dp[i-1][sum -Vm]种; xn =2呢， dp[i-1][sum - 2 * Vm]种。所有的这些情况加起来就是我们的dp[i][sum]。 

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
```
