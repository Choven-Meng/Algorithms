

## [排序算法](https://github.com/Choven-Meng/Algorithms/tree/master/sortAlgorithm/BubbleSort)


## 快速排序

**快速排序的思想：**  
首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。

**一趟快速排序的算法是：**  

快速排序使用分治策略(Divide and Conquer)来把一个序列分为两个子序列。步骤为：

> 1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；    
> 2）以第一个数组元素作为关键数据，赋值给key，即key=A[0]； (基准)   
> 3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；    
> 4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；    
> 5）重复第3、4步，直到i=j； (3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，使得j=j-1，i=i+1，直至找到为止。找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）。

使用快速排序法对一列数字进行排序的过程：　　   
<img src="https://images2015.cnblogs.com/blog/739525/201603/739525-20160328215109269-23458370.gif" alt="">

python实现：

```
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1  # left变为最大值索引位置
        lists[right] = lists[left]
    lists[right] = key  
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
```
二：
```
# 切分点
def partition(array, start, end):
    left, right = start, end
    key = array[left]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] < key:
            left += 1
        array[right] = array[left]

    array[left] = key
    return left


def quickSort(array,left,right):
    if left >= right:
        return array
    index = partition(array, left, right);
    quickSort(array, left, index - 1)
    quickSort(array, index + 1, right);
if __name__ == '__main__':
    alist = [15,54, 26, 93, 17, 77, 31, 44, 55, 100,27]
    print(partition(alist,0,10))
    quickSort(alist,0,10)
```



## 堆排序

堆排序实际上是利用堆的性质来进行排序的，要知道堆排序的原理我们首先一定要知道什么是堆。    
**堆的定义：**    
堆实际上是一棵完全二叉树。     
**堆满足两个性质:**   
1、堆的每一个父节点都大于（或小于）其子节点；    
2、堆的每个左子树和右子树也是一个堆。    
**堆的分类：**     
堆分为两类：     
1、最大堆（大顶堆）：堆的每个父节点都大于其孩子节点；arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]        
2、最小堆（小顶堆）：堆的每个父节点都小于其孩子节点；   arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]  

<img src="https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161217182750011-675658660.png" alt="图片" width="500" height="200">

用数组描述为(大顶堆)：  
arry = [50,45,40,20,25,35,30,10,15]  

**堆排序基本思想和步骤：**

堆排序的基本思想是：将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了。    
* 步骤一 构造初始堆。将给定无序序列构造成一个大顶堆（一般升序采用大顶堆，降序采用小顶堆)。   
  * a.假设给定无序序列结构如下     
  <img src="https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161217192038651-934327647.png" alt="" width="321" height="313">  
  
  * b.此时我们从最后一个非叶子结点开始（叶结点自然不用调整，第一个非叶子结点 arr.length/2-1=5/2-1=1，也就是下面的6结点），从左至右，从下至上进行调整。
  
  <img src="https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161217192209433-270379236.png" alt="" width="697" height="306">  
  
  * c.找到第二个非叶节点4，由于[4,9,8]中9元素最大，4和9交换。      
  
  <img src="https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161217192854636-1823585260.png" alt="" width="700" height="312">      
  
  * d.交换导致了子根[4,5,6]结构混乱，继续调整，[4,5,6]中6最大，交换4和6。   
  
  <img src="https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161217193347886-1142194411.png" alt="" width="747" height="305">      
  
  此时，我们就将一个无需序列构造成了一个大顶堆.      

* 步骤二 将堆顶元素与末尾元素进行交换，使末尾元素最大。然后继续调整堆，再将堆顶元素与末尾元素交换，得到第二大元素。如此反复进行交换、重建、交换。     
  
  * a.将堆顶元素9和末尾元素4进行交换  
  
  <img src="https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161217194207620-1455153342.png" alt="" width="739" height="289">    
  
  * b.重新调整结构，使其继续满足堆定义    
  
  <img src="https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161218153110495-1280388728.png" alt="" width="722" height="272">     
  
  * c.再将堆顶元素8与末尾元素5进行交换，得到第二大元素8.   
  
  <img src="https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161218152929339-1114983222.png" alt="" width="749" height="312">      
  
  * 后续过程，继续进行调整，交换，如此反复进行，最终使得整个序列有序   
  
  <img src="https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161218152348229-935654830.png" alt="" width="439" height="330">  
再简单总结下堆排序的基本思路：

  a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆
   
  b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;
  
  c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。  
  
  堆排序算法的演示：　
  
  <img src="https://images2015.cnblogs.com/blog/739525/201603/739525-20160328213839160-2037856208.gif" alt="">  
  
  python实现：  
  
  ```
  def adjust_heap(lists, i, size):
    leftIndex = 2 * i + 1 # 左子树索引
    rightIndex = 2 * i + 2 # 右子树索引
    maxIndex = i # 最大值索引
    # 选出当前节点与其左右子树的最大值
    if i < size / 2:
        if leftIndex < size and lists[leftIndex] > lists[maxIndex]:
            maxIndex = leftIndex
        if rightIndex < size and lists[rightIndex] > lists[maxIndex]:
            maxIndex = rightIndex
        if maxIndex != i:
            lists[maxIndex], lists[i] = lists[i], lists[maxIndex]
            adjust_heap(lists, maxIndex, size)

def build_heap(lists, size):
    # 对每一个非叶节点向下进行堆调整
    for i in range(int(size/2)-1,-1,-1):
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size) # 建立一个最大堆
    #将堆顶元素与堆的最后一个元素互换，并从堆中去掉最后一个元素
    for i in range(size-1,-1,-1):
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
  ```
