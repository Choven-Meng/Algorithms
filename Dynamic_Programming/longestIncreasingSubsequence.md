


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
        lst = list()
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


```
def LIS(nums):
    a = []
    if nums==[]:
        return 0
    N = len(nums)
    Dp = [1]*N
    for i in range(N-1):

        for j in range(0,i+1):
           
            if nums[i+1]>nums[j]:
                Dp[i+1] = max(Dp[i+1],Dp[j]+1)
                a.append(nums[i+1])
    return max(Dp) 

nums = [10, 9, 2, 5, 3, 7, 101, 18]
LIS(nums)

#output:5
```
