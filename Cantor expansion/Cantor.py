"""
计算康托展开值

input:34152
return:61
"""
# 阶乘计算
def func(num):
    count = 1
    for i in range(1, num + 1):
        count = count * i
    return count

def contor(a):
    x = 0
    n = len(a)
    for i in range(n):
        # 小于当前值的个数
        smaller = 0
        for j in range(i+1,n):
            if a[j] < a[i]:
                smaller += 1

        x += func(n-i-1)*smaller
    # 康托展开值
    return x

if __name__ =='__main__':
    a = input()
    print(contor(a))
