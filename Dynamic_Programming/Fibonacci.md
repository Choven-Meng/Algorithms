
斐波那契数列 又称 黄金分割数列 ，因为该数列是以兔子繁殖为例子而引入，故又称为 “兔子数列” ，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……

在数学上，斐波纳契数列以如下被以递归的方法定义：F(0)=1，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）

```
def fibonacci(N):
    fib_array = []
    if N:
        N = int(N)
        fib_array.append(0)
        fib_array.append(1)
        for i in range(2, N + 1):
            fib_array.append(fib_array[i - 1] + fib_array[i - 2])
    elif N == 0:
        fib_array.append(0)
    return fib_array

fibonacci(10)
#output:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

快速计算第n个斐波那契数，O(log(n))
```
# return F(n)
def fibonacci(n: int):  # noqa: E999 This syntax is Python 3 only
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    return _fib(n)[0]


# returns (F(n), F(n-1))
def _fib(n: int):  # noqa: E999 This syntax is Python 3 only
    if n == 0:
        # (F(0), F(1))
        return (0, 1)
    else:
        # F(2n) = F(n)[2F(n+1) − F(n)]
        # F(2n+1) = F(n+1)^2+F(n)^2
        a, b = _fib(n // 2) # 整数
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

fibonacci(10)
#output :55
```
