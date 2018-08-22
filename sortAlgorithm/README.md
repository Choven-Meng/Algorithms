

## [排序算法](https://github.com/Choven-Meng/Algorithms/tree/master/sortAlgorithm/BubbleSort)


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
