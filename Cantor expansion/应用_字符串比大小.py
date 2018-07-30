"""
现在有"abcdefghijkl”12个字符，将其所有的排列中按字典序排列，给出任意一种排列，说出这个排列在所有的排列中是第几小的？
eg:

input:
第一行有一个整数n（0＜n＜=10000）;
随后有n行，每行是一个排列；
3
abcdefghijkl
hgebkflacdji
gfkedhjblcia

output:
输出一个整数m，占一行，m表示排列是第几位；
1
302715242
260726926
"""


from functools import reduce
# 阶乘计算1
def factorial(n):
    return reduce(lambda x,y: x*y, (x for x in range(1, n+1)), 1)
# 阶乘计算2
def PermutationNumber(num):
    count = 1
    for i in range(1, num + 1):
        count = count * i
    return count

# 需要计算康托展开的字符串首字母所在的索引位置
def FirstCharPosition(instr):
    clist = []
    for c in instr:
        clist.append(c)
    clist.sort()
    return clist.index(instr[0])

# 计算康托展开值
def Compare(instr):
    if len(instr) == 1:
        return 1
    return FirstCharPosition(instr) * PermutationNumber(len(instr) - 1) + Compare(instr[1:])# 回归迭代


if __name__ == "__main__":
    number = int(input().strip())
    list = []
    for i in range(number):
        list.append(raw_input().strip())
    for i in range(number):
        print (Compare(list[i]))
 
