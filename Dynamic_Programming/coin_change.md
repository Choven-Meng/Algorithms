
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
