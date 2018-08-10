
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
