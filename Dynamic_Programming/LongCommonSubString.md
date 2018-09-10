最长公共子串(The Longest Common Substring)

问题描述：   
给定两个字符串，求出它们之间最长的连续相同子字符串的长度。

举个例子：  
'abcdfg','abdfg'的最长公共子串是‘dfg’

最直接的解法自然是找出两个字符串的所有子字符串进行比较看他们是否相同，然后取得相同最长的那个。对于一个长度为n的字符串，它有n(n+1)/2 个非空子串。所以假如两个字符串的长度同为n，通过比较各个子串其算法复杂度大致为O(n4)。这还没有考虑字符串比较所需的时间。简单想想其实并不需要取出所有的子串，而只要考虑每个子串的开始位置就可以，这样可以把复杂度减到O(n3)。   
但这个问题最好的解决办法是动态规划法，在后边会更加详细介绍这个问题使用动态规划法的契机：有重叠的子问题。进而可以通过空间换时间，让复杂度优化到O(n2)，代价是空间复杂度从O(1)一下子提到了O(n2)。   
从时间复杂度的角度讲，对于最长公共子串问题，O(n2)已经是目前我所知最优的了，也是面试时所期望达到的。但是对于空间复杂度O(n2)并不算什么，毕竟算法上时间比空间更重要，但是如果可以省下一些空间那这个算法就会变得更加美好。所以进一步的可以把空间复杂度减少到O(n)，这是相当美好了。但有一个算法可以让该问题的空间复杂度减少回原来的O(1)，而时间上如果幸运还可以等于O(n)。

最长公共子串问题就是求两个字符串最长公共子串的问题。

### 1、暴力法

这种暴力解法唯一值得学习的地方，就是怎么求一个字符串的所有子字符串。用一个二层循环即可，外面一层循环从字符串的头遍历到尾，里面的循环就从当前的位置开始，每个字符地加，这样就可以得到所有的子字符串了。
```
def getLongestSubstring(str1,str2):
    longest=0 # 公共子串的长度
    start_pos1=-1 # str1的起始位置
    start_pos2=-1 # str2的起始位置
    compares=0   # 记录比较次数

    for i in range(len(str1)):
        for j in range(len(str2)):
            length=0
            m=i
            n=j
            while str1[m]==str2[n]:
                compares+=1
                length+=1
                m+=1
                n+=1
                if (m>=len(str1))|(n>=len(str2)):
                    break
            if longest<length:
                compares+=1
                longest=length
                start_pos1=i
                start_pos2=j
    return longest,start_pos1,start_pos2,compares

str1 = 'abcdfg'
str2 = 'abdfg'
getLongestSubstring(str1,str2)

#output：
(3, 3, 2, 11)
```

### 2、动态规划

解法就是用一个矩阵来记录两个字符串中所有位置的两个字符之间的匹配情况，若是匹配则为1,否则为0。然后求出对角线最长的1的序列，其对应的位置就是最长匹配子串的位置。

```
def find_lcsubstr(s1, s2): 
	m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  #生成0矩阵，为方便后续计算，比字符串长度多了一列
	mmax=0   #最长匹配的长度
	p=0  #最长匹配对应在s1中的最后一位

	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i]==s2[j]:
				m[i+1][j+1]=m[i][j]+1
                # 计算最大长度
				if m[i+1][j+1]>mmax:
					mmax=m[i+1][j+1]
					p=i+1

	return s1[p-mmax:p],mmax   #返回最长子串及其长度

 
find_lcsubstr('abcdfg','abdfg')

# output:('dfg', 3)
```





阿里算法笔试题：

输入:输入数据包含两行，第一行，实体列表，多种实体之间用分号隔开，实体名和实体值之间用下划线隔开，多个实体值之间用竖线隔开，所有标点都是英文状态下的，格式如下：实体名称1_实体值1|实体值2|…;实体名称2_实体值1|实体值2|…;… 第二行，用户的自然语言指令   

输出:被标记了关键词的指令。指令中的关键词前后加一个空格被单独分出来，并在后面跟上"/"+实体名称来标记。如果一个实体值属于多个实体，将这些实体都标记出来，并按照实体名称的字符串顺序正序排列，并以逗号分隔。

输入范例:singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪请播放周杰伦的七里香给我听   
请播放周杰伦的七里香给我听   

输出范例:请播放 周杰伦/actor,singer 的 七里香/song 给我听

```
def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2+1)] for j in range(lstr1+1)]  
    maxNum = 0        
    p = 0              
    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                record[i+1][j+1] = record[i][j] + 1
         
    return str1[p-maxNum:p]   



input1 = input()
input2 = input()


inputdict = {}
for i in input1.split(';'):
    a = i.split('_')
    inputdict[a[0]] = a[1]

dic = {}
for key,val in inputdict.items():
    comStr = getNumofCommonSubstr(val,input2)
    if comStr in dic.keys():
        dic[comStr] = dic[comStr] + ',' + key
    else:
        dic[comStr] = key
        
for key,val in dic.items():
    if key in input2:
        inp = ' '+key+'/'+val+' '
        input2 = input2.replace(key,inp)
print (input2)

# input
singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪

请播放周杰伦的七里香给我听

# output
'请播放 周杰伦/singer,actor 的 七里香/song 给我听'
```
