
### 反转链表

链表的翻转是程序员面试中出现频度最高的问题之一，常见的解决方法分为递归和迭代两种。   
我们知道迭代是从前往后依次处理，直到循环到链尾；而递归恰恰相反，首先一直迭代到链尾也就是递归基判断的准则，然后再逐层返回处理到开头。总结来说，链表翻转操作的顺序对于迭代来说是从链头往链尾，而对于递归是从链尾往链头。下面我会用详细的图文来剖析其中实现的细节。   

1、非递归（迭代）方式    

　　迭代的方式是从链头开始处理，如下图给定一个存放5个数的链表。  

[链表反转](https://blog.csdn.net/fx677588/article/details/72357389)
