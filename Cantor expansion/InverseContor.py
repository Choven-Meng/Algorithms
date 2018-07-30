"""
逆康托展开计算
根据排位数-1计算排列组合
input:61 (康托展开值，排位数减1)
return:34152  
"""
# 阶乘计算
def func(num):
    count = 1
    for i in range(1, num + 1):
        count = count * i
    return count

def InverseContor(n,v = [1,2,3,4,5]):
    """
    :param init: 初始排列 ,默认是[1,2,3,4,5]
    :param n: 排位数
    :return:  排列组合
    """
    a = [] # 所求排列组合
    m = len(v)
    for i in range(m,0,-1):
        r = n % func(i-1) # 余数
        t = int(n / func(i-1)) # 除数,即比当前位小的数有t个
        n = r
        sorted(v)  # 从小到大排列
        a.append(v[t]) #剩余数里第t+1个为当前位的数
        v.pop(t) # 移除当前位的数
    return a


if __name__ =='__main__':
    n = int(input())
    print(InverseContor(n))
