最长递增子序列

问题描述：  
给定一串数组，返回其中的最长递增子序列的长度。例如：给定数组[10, 9, 2, 5, 3, 7, 101, 18],则其最长递增子序列为[2, 3, 7, 101],返回长度4.

思路：  
用Dp[i]来保存从0-i的数组的最长递增子序列的长度。如上数组Dp[0]=1,Dp[1]=1,Dp[2]=1,Dp[3]=2,Dp[4]=2。。。计算Dp[i]的值可以对Dp[i]之前数值进行遍历，如果nums[i]>nums[j],则Dp[i] = max(Dp[i],Dp[j]+1)。复杂度为O(n*n)

```
def LIS(nums):
    if nums==[]:
        return 0
    N = len(nums)
    Dp = [1]*N
    for i in range(N-1):

        for j in range(0,i+1):
           
            if nums[i+1]>nums[j]:
                Dp[i+1] = max(Dp[i+1],Dp[j]+1)
    return max(Dp) 

nums = [10, 9, 2, 5, 3, 7, 101, 18]
LIS(nums)

#output:5
```
-------------------------------------

下面这种方法的时间复杂度是O(nlogn)。具体的方法是：采用lst[]数组用来存放上升子序列（上面的方法是用来存放当前数的最大上升子序列），还是nums[]={1,7,3,5,9,4,8}，想要找出最长的子序列，那么每一个值都要尽可能小，比如说{1,3}一定比{1,7}好，那么，在遍历到7的时候，lst=[1,7]，这时遍历3,3比7小（3的潜力更大），应该用3代替7，也就是在数组nums[1,7]中找到3的位置，采用二分法（时间 复杂度O(logn)）。具体程序：

```
class LIS:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums == None or len(nums) ==0:
            return 0
        lst = []
        for i in range(len(nums)):
            if len(lst) == 0 or lst[len(lst) - 1] <= nums[i]:
                lst.append(nums[i])
            else:
                index = self.findFirstLargeEqual(lst,nums[i])
                lst[index] = nums[i]
        return len(lst),lst
    
    # 二分法
    def findFirstLargeEqual(self,lst,target):
        left = 0
        right = len(lst) -1 
        while left < right:
            mid = int((left + right)/2)
            if lst[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

nums = [10, 9, 2, 5, 3, 7, 101, 18]
LIS().longestIncreasingSubsequence(nums)

# output:
(4, [2, 3, 7, 18])
```


