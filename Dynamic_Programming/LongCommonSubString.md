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
                if record[i+1][j+1] > maxNum:
                    maxNum = record[i+1][j+1]
                    p = i + 1
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
