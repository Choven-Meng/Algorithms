**海量数据中找出前k大数(topk问题)**

&emsp;&emsp;先拿10000个数建堆，然后一次添加剩余元素，如果大于堆顶的数（10000中最小的），将这个数替换堆顶，并调整结构使之仍然是一个最小堆，这样，遍历完后，堆中的10000个数就是所需的最大的10000个。建堆时间复杂度是O（mlogm），算法的时间复杂度为O（nmlogm）（n为10亿，m为10000）。

&emsp;&emsp;优化的方法：可以把所有10亿个数据分组存放，比如分别放在1000个文件中。这样处理就可以分别在每个文件的10^6个数据中找出最大的10000个数，合并到一起在再找出最终的结果。

**top K问题**

&emsp;&emsp;在大规模数据处理中，经常会遇到的一类问题：在海量数据中找出出现频率最好的前k个数，或者从海量数据中找出最大的前k个数，这类问题通常被称为top K问题。例如，在搜索引擎中，统计搜索最热门的10个查询词；在歌曲库中统计下载最高的前10首歌等。

&emsp;&emsp;针对top K类问题，通常比较好的方案是分治+Trie树/hash+小顶堆（就是上面提到的最小堆），即先将数据集按照Hash方法分解成多个小数据集，然后使用Trie树活着Hash统计每个小数据集中的query词频，之后用小顶堆求出每个数据集中出现频率最高的前K个数，最后在所有top K中求出最终的top K。

**eg：有1亿个浮点数，如果找出期中最大的10000个？**

&emsp;&emsp;最容易想到的方法是将数据全部排序，然后在排序后的集合中进行查找，最快的排序算法的时间复杂度一般为O（nlogn），如快速排序。但是在32位的机器上，每个float类型占4个字节，1亿个浮点数就要占用400MB的存储空间，对于一些可用内存小于400M的计算机而言，很显然是不能一次将全部数据读入内存进行排序的。其实即使内存能够满足要求（我机器内存都是8GB），该方法也并不高效，因为题目的目的是寻找出最大的10000个数即可，而排序却是将所有的元素都排序了，做了很多的无用功。

&emsp;&emsp;第二种方法为局部淘汰法，该方法与排序方法类似，用一个容器保存前10000个数，然后将剩余的所有数字——与容器内的最小数字相比，如果所有后续的元素都比容器内的10000个数还小，那么容器内这个10000个数就是最大10000个数。如果某一后续元素比容器内最小数字大，则删掉容器内最小元素，并将该元素插入容器，最后遍历完这1亿个数，得到的结果容器中保存的数即为最终结果了。此时的时间复杂度为O（n+m^2），其中m为容器的大小，即10000。

&emsp;&emsp;第三种方法是分治法，将1亿个数据分成100份，每份100万个数据，找到每份数据中最大的10000个，最后在剩下的100*10000个数据里面找出最大的10000个。如果100万数据选择足够理想，那么可以过滤掉1亿数据里面99%的数据。100万个数据里面查找最大的10000个数据的方法如下：用快速排序的方法，将数据分为2堆，如果大的那堆个数N大于10000个，继续对大堆快速排序一次分成2堆，如果大的那堆个数N大于10000个，继续对大堆快速排序一次分成2堆，如果大堆个数N小于10000个，就在小的那堆里面快速排序一次，找第10000-n大的数字；递归以上过程，就可以找到第1w大的数。参考上面的找出第1w大数字，就可以类似的方法找到前10000大数字了。此种方法需要每次的内存空间为10^6*4=4MB，一共需要101次这样的比较。

&emsp;&emsp;第四种方法是Hash法。如果这1亿个书里面有很多重复的数，先通过Hash法，把这1亿个数字去重复，这样如果重复率很高的话，会减少很大的内存用量，从而缩小运算空间，然后通过分治法或最小堆法查找最大的10000个数。

&emsp;&emsp;第五种方法采用最小堆。首先读入前10000个数来创建大小为10000的最小堆，建堆的时间复杂度为O（mlogm）（m为数组的大小即为10000），然后遍历后续的数字，并于堆顶（最小）数字进行比较。如果比最小的数小，则继续读取后续数字；如果比堆顶数字大，则替换堆顶元素并重新调整堆为最小堆。整个过程直至1亿个数全部遍历完为止。然后按照中序遍历的方式输出当前堆中的所有10000个数字。该算法的时间复杂度为O（nmlogm），空间复杂度是10000（常数）。

&emsp;&emsp;top K问题很适合采用MapReduce框架解决，用户只需编写一个Map函数和两个Reduce 函数，然后提交到Hadoop（采用Mapchain和Reducechain）上即可解决该问题。具体而言，就是首先根据数据值或者把数据hash(MD5)后的值按照范围划分到不同的机器上，最好可以让数据划分后一次读入内存，这样不同的机器负责处理不同的数值范围，实际上就是Map。得到结果后，各个机器只需拿出各自出现次数最多的前N个数据，然后汇总，选出所有的数据中出现次数最多的前N个数据，这实际上就是Reduce过程。对于Map函数，采用Hash算法，将Hash值相同的数据交给同一个Reduce task；对于第一个Reduce函数，采用HashMap统计出每个词出现的频率，对于第二个Reduce 函数，统计所有Reduce task，输出数据中的top K即可。

**以下是一些经常被提及的该类问题。**

（1）有10000000个记录，这些查询串的重复度比较高，如果除去重复后，不超过3000000个。一个查询串的重复度越高，说明查询它的用户越多，也就是越热门。请统计最热门的10个查询串，要求使用的内存不能超过1GB。

（2）有10个文件，每个文件1GB，每个文件的每一行存放的都是用户的query，每个文件的query都可能重复。按照query的频度排序。

（3）有一个1GB大小的文件，里面的每一行是一个词，词的大小不超过16个字节，内存限制大小是1MB。返回频数最高的100个词。

（4）提取某日访问网站次数最多的那个IP。

（5）10亿个整数找出重复次数最多的100个整数。

（6）搜索的输入信息是一个字符串，统计300万条输入信息中最热门的前10条，每次输入的一个字符串为不超过255B，内存使用只有1GB。

（7）有1000万个身份证号以及他们对应的数据，身份证号可能重复，找出出现次数最多的身份证号。

**Top K问题的两种解决思路:**

* 最直观：小顶堆（大顶堆 -> 最小100个数）；

* 较高效：Quick Select算法。

1. 堆[小顶堆(TopK大)/大顶堆(BtmK小)]

小顶堆（min-heap）有个重要的性质——每个结点的值均不大于其左右孩子结点的值，则堆顶元素即为整个堆的最小值。在Python中对堆这种数据结构进行了模块化，我们可以通过调用heapq模块来建立堆这种数据结构，同时heapq模块也提供了相应的方法来对堆做操作。 

* 求出TopK大的元素，使用小顶堆，heapq模块实现  

```
import heapq
import random

class TopkHeap(object):
    def __init__(self,k):
        self.k = k
        self.data = [] #建立一个堆

    def Push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem) # 往堆中插入数据
        else:
            topk_small = self.data[0]
            if elem > topk_small:
                heapq.heapreplace(self.data, elem) #弹出一个最小的值，然后将elem插入到堆当中

    def TopK(self):
        return [x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]

if __name__ == "__main__":
    list_rand = random.sample(range(1000000), 100)
    th = TopkHeap(3)
    for i in list_rand:
        th.Push(i)
    print (th.TopK())

```
Python自带的heapq模块实现的是最小堆，没有提供最大堆的实现,方法是：push(e)改为push(-e)，pop(e)为-pop(e)，也就是说存入和取出的数都是相反数，其他逻辑和TopK相同。

* Quick Select

Quick Select 脱胎于快排（Quick Sort），两个算法的作者都是Hoare，并且思想也非常接近：选取一个基准元素pivot，将数组切分（partition）为两个子数组，比pivot大的扔左子数组，比pivot小的扔右子数组，然后递推地切分子数组。Quick Select不同于Quick Sort的是其没有对每个子数组做切分，而是对目标子数组做切分。其次，Quick Select与Quick Sort一样，是一个不稳定的算法；pivot选取直接影响了算法的好坏，worst case下的时间复杂度达到了O(n2)。下面给出Quick Sort的python实现： 

```
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
Quick Select的目标是找出第k大元素，所以

* 若切分后的左子数组的长度 > k，则第k大元素必出现在左子数组中；

* 若切分后的左子数组的长度 = k-1，则第k大元素为pivot；

* 若上述两个条件均不满足，则第k大元素必出现在右子数组中。

Quick Select的python实现如下：
```
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

def minTopK(array, m):
    start, end = 0, len(array) - 1
    index = partition(array, start, end)
    while index != m:
        if index < m:
            index = partition(array, index+1, end)
        else:
            index = partition(array, start, index)

    return array[:m]

if __name__ == '__main__':
    alist = [15,54, 26, 93, 17, 77, 31, 44, 55, 100]
    print(partition(alist,0,9))
    print(minTopK(alist,  3))
```

更为简单直观的方法：

```
def partition(seq):
    pi, seq = seq[0], seq[1:]                 # 选取并移除主元
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def select(seq, k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k: return pi
    if m < k: return select(hi, k-m-1)
    return select(lo, k)
```
