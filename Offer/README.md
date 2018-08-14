
[一. 数组](#一-数组)

  * [1. 不用加减乘除做加法](#1-二维数组中的查找)  

[二. 字符串](#二-字符串)

  * [1. 替换空格](#1-替换空格)  
  
[三. 链表](#三-链表)

  * [1. 从尾到头打印链表](#1-从尾到头打印链表) 
  
[四. 树](#四-树)

  * [1. 重建二叉树](#1-重建二叉树) 
  
[五. 栈和队列](#五-栈和队列)

  * [1. 用两个栈实现队列](#1-用两个栈实现队列) 
  
[六. 查找和排序](#六-查找和排序)

  * [1. 旋转数组的最小数字](#1-旋转数组的最小数字) 

[七. 递归和循环](#七-递归和循环)

  * [1. 斐波那契数列](#1-斐波那契数列)   
  * [2. 变态跳台阶](#2-变态跳台阶)   
  * [3. 跳台阶](#3-跳台阶)
  * [4. 矩形覆盖](#4-矩形覆盖)
  
[八. 位运算](#八-位运算)

  * [1. 二进制中1的个数](#1-二进制中1的个数)
  
[九. 代码的完整性](#九-代码的完整性)

  * [1. 调整数组顺序使奇数位于偶数前面](#1-调整数组顺序使奇数位于偶数前面) 
  
[十. 代码的鲁棒性](#十-代码的鲁棒性)

  * [1. 链表中倒数第k个节点](#1-链表中倒数第k个节点)    
  * [2. 反转链表](#2-反转链表)   
  * [3. 合并两个排序的链表](#3-合并两个排序的链表)   
  * [4. 树的子结构](#4-树的子结构)  
  
[十一. 面试思路](#十一-面试思路)

  * [1. 二叉树的镜像](#1-二叉树的镜像)

[十二. 画图让抽象形象化](#十二-画图让抽象形象化)

  * [1. 顺时针打印矩阵](#1-顺时针打印矩阵)
  
[十三. 举例让抽象具体化](#十三-举例让抽象具体化)

  * [1. 包含min函数的栈](#1-包含min函数的栈)   
  * [2. 栈的压入、弹出序列](#2-栈的压入、弹出序列)   
  * [3. 从上往下打印二叉树](#3-从上往下打印二叉树)
  * [4. 二叉搜索树的后序遍历序列](#4-二叉搜索树的后序遍历序列)
  

## 一. 数组

* ### 1. 二维数组中的查找

#### 题目描述

题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。   
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


```
方法一： 循环迭代查找，不是最优
284ms
5760k
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return
        row = len(array)
        col = len(array[0])

        for i in range(row):
            for j in range(col):
                if target == array[i][j]:
                    return True

        return False
```

```
方法二：上述方法的时间复杂度是O(n^2)，最优化的方式是从左下或者右上开始搜索
从右上开始搜索，如果数组中的数比该数要大，那么想左移动一位，如果数组中的数比该数小，向下移动一位，
因为数组本身是从左到右依次增大，从上到下一次增大
281ms
5644k

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        raw = len(array)
        col = len(array[0])

        i = 0
        j = col - 1
        while i < raw and j >= 0:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return False
```

## 二. 字符串

* ### 1. 替换空格

**题目描述**

题目：请实现一个函数，将一个字符串中的空格替换成“%20”。  
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

```
方法1： 使用replace
24ms
5624k
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')
```

## 三. 链表
 
* ### 1. 从尾到头打印链表

**题目描述**

输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

```
方法一：使用extend，在尾部插入，其实最关键在于[::-1],只不过输入数据多样化，有可能还是集合，所以转成列表
这个方法效率应该还可以，先存入vector，再反转vector
26ms
5512k

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        result = []
        while listNode.next is not None:
            result.extend([listNode.val])
            listNode = listNode.next
        result.extend([listNode.val])

        return result[::-1]
```

```
方法二： 使用insert直接在头部插入
26ms
6336k

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        result = []
        head = listNode

        while head:
            result.insert(0, head.val)
            head = head.next
        return result
 ```
 
 ## 四. 树
 
* ### 1. 重建二叉树

**题目描述**

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。  
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

```
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        val = tin.index(pre[0])

        # 可以动手试一下啊，第一个参数
        root.left = self.reConstructBinaryTree(pre[1:val + 1], tin[:val])
        root.right = self.reConstructBinaryTree(pre[val + 1:], tin[val + 1:])
        return root
```

## 五. 栈和队列
 
* ### 1. 用两个栈实现队列

**题目描述**

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

```
有两个栈stackA、stackB，A是入栈的，B是出栈的，入栈时，直接进入A即可，出栈时，先判断是否有元素，
如果B没有元素，pop肯定报错，应该先将A中所有的元素压倒B里面，再pop最上面一个元素，如果B中有就直接pop出，就可以，
这是最优的思路，两个栈实现了先进后出，在一起又实现了队列的先进先出。
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        # write code here
        self.stackA.append(node)
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
```

## 六. 查找和排序
 
* ### 1. 旋转数组的最小数字

**题目描述**

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

```
不考虑旋转数组特性的话，直接用min(array);
考虑旋转数组的特性就比较复杂，在算法上，考虑数字没有重复的情况的话，旋转后的数组可以划分为两个有序的子数组：前面子数组的大小都大于后面子数组的大小，
实际最小的元素就是两个子数组的分界线。使用二分法，有两个指针，第一个指针指向front，第二个指针指向rear，midIndex是中间数字，按照题目的旋转规则，
第一个首位一定大于中间位，否则就不是旋转数组。前面数字向后移动，不断迭代，当首位和最后位只差1时，最后维就是最小值。此时最坏时间复杂度是O(logn),
但是要考虑数字重复的话，情况只可能是首位和末尾和中间重这种[1,0,1,1]只能取其中最小值，逐一排列，对于首位和中间位重的，比如[1,1,0],
把首位移动到后面去，可以处理，或者中间位和末尾重，比如[1,0,0]，也是能处理，其他情况不存在，因为前提要求是旋转数组。

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        front, rear = 0, len(rotateArray) - 1
        midIndex = 0
        while rotateArray[front] >= rotateArray[rear]:
            if rear - front == 1:
                midIndex = rear
                break
            midIndex = (front + rear) // 2
            if rotateArray[front] == rotateArray[midIndex] and rotateArray[front] == rotateArray[rear]:
                return self.minOrder(rotateArray, front, rear)

            if rotateArray[front] <= rotateArray[midIndex]:
                front = midIndex
            elif rotateArray[rear] >= rotateArray[midIndex]:
                rear = midIndex
        return rotateArray[midIndex]

    def minOrder(self, array, front, end):
        result = array[0]
        for i in array[front:end + 1]:
            if i < result:
                result = i
        return result
```

## 七. 递归和循环
 
* ### 1. 斐波那契数列

**题目描述**

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39

```
斐波那契数列：1,1,2,3,5,8，···       F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
第三位是前两位之和
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0,1]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]
```

* ### 2. 变态跳台阶

**题目描述**

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

```
因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
跳1级，剩下n-1级，则剩下跳法是f(n-1)
跳2级，剩下n-2级，则剩下跳法是f(n-2)
所以f(n)=f(n-1)+f(n-2)+...+f(1)
因为f(n-1)=f(n-2)+f(n-3)+...+f(1)
所以f(n)=2*f(n-1)
然后求解这个无穷级数的和，正确答案应该是：每次至少跳一个，至多跳n个，一共有f(n)=2的n-1次方种跳法

class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)
 
 用递归：递归时间长，不建议用
 class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        return 2*self.jumpFloorII(number-1)
```

* ### 3. 跳台阶

**题目描述**

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

```
对于本题,前提只有 一次 1阶或者2阶的跳法。
a.如果两种跳法，1阶或者2阶，那么假定第一次跳的是一阶，那么剩下的是n-1个台阶，跳法是f(n-1);
b.假定第一次跳的是2阶，那么剩下的是n-2个台阶，跳法是f(n-2)
c.由a\b假设可以得出总跳法为: f(n) = f(n-1) + f(n-2) 
d.然后通过实际的情况可以得出：只有一阶的时候 f(1) = 1 ,只有两阶的时候可以有 f(2) = 2
e.可以发现最终得出的是一个斐波那契数列：
        
       | 1, (n=1)
f(n) = | 2, (n=2)
       | f(n-1)+f(n-2) ,(n>2,n为整数)

class Solution:
    def jumpFloor(self, number):
        # write code here
        res = [1,2]
        while len(res) <= number:
            res.append(res[-1]+res[-2])
        if number == 1:
            return 1
        else:
            return res[number-1]
```

* ### 4. 矩形覆盖

**题目描述**

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？  
```
依旧是斐波那契数列
2*n的大矩形，和n个2*1的小矩形
其中 2*target 为大矩阵的大小
有以下几种情形：
1⃣️target <= 0 大矩形为<= 2*0,直接return 1；
2⃣️target = 1大矩形为2*1，只有一种摆放方法，return1；
3⃣️target = 2 大矩形为2*2，有两种摆放方法，return2；
4⃣️target = n 分为两步考虑：
第一次摆放一块 2*1 的小矩阵，则摆放方法总共为f(target - 1)
第一次摆放一块1*2的小矩阵，则摆放方法总共为f(target-2)
因为，摆放了一块1*2的小矩阵（用√√表示），对应下方的1*2（用××表示）摆放方法就确定了，所以为f(targte-2)
target >= 3  f(n) = f(target - 1) + f(targte-2)

class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            res = [0,1,2]
            while len(res) <= number:
                res.append(res[-1]+res[-2])
            return res[number]
```

## 八. 位运算
 
* ### 1. 二进制中1的个数

**题目描述**

输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。    
```
如果一个整数不为0，那么这个整数至少有一位是1。如果我们把这个整数减1，那么原来处在整数最右边的1就会变为0，原来在1
后面的所有的0都会变成1(如果最右边的1后面还有0的话)。其余所有位将不会受到影响。
举个例子：一个二进制数1100，从右边数起第三位是处于最右边的一个1。减去1后，第三位变成0，它后面的两位0变成了1，
而前面的1保持不变，因此得到的结果是1011.我们发现减1的结果是把最右边的一个1开始的所有位都取反了。这个时候如果我们
再把原来的整数和减去1之后的结果做与运算，从原来整数最右边一个1那一位开始所有位都会变成0。如1100&1011=1000.也就是
说，把一个整数减去1，再和原整数做与运算，会把该整数最右边一个1变成0.那么一个整数的二进制有多少个1，就可以进行多少
次这样的操作。
但是负数使用补码表示的，对于负数，最高位为1，而负数在计算机是以补码存在的，往右移，符号位不变，符号位1往右移，
最终可能会出现全1的情况，导致死循环。与0xffffffff相与，就可以消除负数的影响

class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n<0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = n & (n-1)
        return count
```

## 九. 代码的完整性
 
* ### 1. 调整数组顺序使奇数位于偶数前面

**题目描述**

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。   
```
class Solution:
    def reOrderArray(self, array):
        # write code here

        res1 = []
        res2 = []
        for i in array:
            if i % 2 == 0:
                res1.append(i)
            else:
                res2.append(i)
        return res2 + res1
```

## 十. 代码的鲁棒性
 
* ### 1. 链表中倒数第k个节点

**题目描述**

输入一个链表，输出该链表中倒数第k个结点   
```
使用列表的切片，还是很快的

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        while head:
            res.append(head)
            head = head.next
        if k > len(res) or k < 1:
            return
        return res[-k]
```

* ### 2. 反转链表

**题目描述**

输入一个链表，反转链表后，输出新链表的表头。   
```
链表的翻转，例如 1->2->3->4->5  ==>  5->4->3->2->1

方法一:迭代(链表翻转操作的顺序对于迭代来说是从链头往链尾)
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        newHead = None
        while pHead:
            tem = pHead.next  #暂存pHead下一个地址，防止变化指针指向后找不到后续的数
            pHead.next = newHead   #pHead->next指向前一个空间
            newHead = pHead  #新链表的头移动到p，扩长一步链表
            pHead = tem  #pHead指向原始链表pHead指向的下一个空间
        return newHead
```    
```
方法二：递归(链表翻转操作的顺序对于递归来说是从链尾往链头)
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        newHead = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return newHead
```
 
* ### 3. 合并两个排序的链表

**题目描述**

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。   
```
方法一：递归版本，注意比较很好理解

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1

        mergepHead = None
        if pHead1.val <= pHead2.val:
            mergepHead = pHead1
            mergepHead.next = self.Merge(pHead1.next, pHead2)
        elif pHead1.val > pHead2.val:
            mergepHead = pHead2
            mergepHead.next = self.Merge(pHead1, pHead2.next)

        return mergepHead

```   
```
版本二：非递归版本

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        dummy = ListNode(0)
        pHead = dummy

        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                dummy.next = pHead2
                pHead2 = pHead2.next
            else:
                dummy.next = pHead1
                pHead1 = pHead1.next

            dummy = dummy.next
        if pHead1:
            dummy.next = pHead1
        elif pHead2:
                dummy.next = pHead2
        return pHead.next
 ```


* ### 4. 树的子结构

**题目描述**  

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）   
```
分析，两个序列才能确定一个树，所以先用先序遍历，再用字符串进行匹配是不对的，因为的树的结构你确定不了。这一题，首先判断根节点是不是相同，不相同是一个递归，把pRoot1的左右子树一次和PRoot2进行判断,如果根节点相同，那么进入下一个函数，接着判断，左边节点的下一级和左边子树下一级是不是相同，又是一个递归。
两个递归操作

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        # 判断根节点
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.same(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def same(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        # 这一步不断判断下一个节点，因为是递归操作。
        if pRoot1.val != pRoot2.val:
            return False
        return self.same(pRoot1.left, pRoot2.left) and self.same(pRoot1.right, pRoot2.right)
```

## 十一. 面试思路
 
* ### 1. 二叉树的镜像

**题目描述**
  
 操作给定的二叉树，将其变换为源二叉树的镜像。  
 ```
 二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
     
 # class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        root.left,root.right = root.right,root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
 ```
 
 ## 十二. 画图让抽象形象化
 
* ### 1. 顺时针打印矩阵

**题目描述**

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16，则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.   
```
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while (matrix):
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        newmat = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(col):
            newmat1 = []
            for j in range(row):
                newmat1.append(matrix[j][i])
            newmat.append(newmat1)
        newmat.reverse()
        return newmat
```

## 十三. 举例让抽象具体化
 
* ### 1. 包含min函数的栈

**题目描述**

定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。  
```
我们可以设计两个栈：Stack和StackMin，一个就是普通的栈，另外一个存储push进来的最小值。
首先是push操作：
每次压入的数据newNum都push进Stack中，然后判断StackMin是否为空，如果为空那也把newNum同步压入StackMin里；
如果不为空，就先比较newNum和StackMin中栈顶元素的大小，如果newNum较大，那就不压入StackMin里，只压入一个最小值
否则就同步压入StackMin里。弹出时，同步弹出，这是一个栈结构。

class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())
    def pop(self):
        # write code here
        if self.minstack == [] or self.stack == []:
            return None
        self.minstack.pop()
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]
```

* ### 2. 栈的压入、弹出序列

**题目描述**

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）   
```
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while popV:
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True
```

* ### 3. 从上往下打印二叉树

**题目描述**

从上往下打印出二叉树的每个节点，同层节点从左至右打印  
```
广度优先层次遍历，利用一个队列来实现
层序遍历的基本过程是：
先根节点入队，然后：
1.从队列中取出一个元素
2.访问该元素所指的结点
3.若该元素所指结点的左、右孩子结点非空，则将其左、右孩子的指针顺序入队
利用队列，首先将根节点放入队列中，取队列的首节点，把值存进列表，然后考虑左右指针，把指针放进列表，再存值

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = []
        result = []

        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
```

* ### 4. 二叉搜索树的后序遍历序列

**题目描述**

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。   
```
二叉搜索树即是二叉排序树，
1. 后序遍历序列的最后一个元素为二叉树的根节点；
2. 二叉搜索树左子树上所有的结点均小于根结点、右子树所有的结点均大于根结点。
算法步骤如下：
1. 找到根结点；
2. 遍历序列，找到第一个大于等于根结点的元素i，则i左侧为左子树、i右侧为右子树；
3. 我们已经知道i左侧所有元素均小于根结点，那么再依次遍历右侧，看是否所有元素均大于根结点；若出现小于根结点的元素，则直接返回false；若右侧全都大于根结点，则：
4. 分别递归判断左/右子序列是否为后序序列

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        root = sequence[-1]
        i = 0
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1
        for node in sequence[i:-1]:
            if node < root:
                return False

        left = True
        # i>0 意味i =0 或者1 的时候，两个元素在二叉树没有排序之分的，但是3个元素就有了左右子树之分
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        right = True
        # len(sequence)>3才有左右之分的
        if i < len(sequence) - 2 and left:
            right = self.VerifySquenceOfBST(sequence[i + 1:])

        return left and right

```
