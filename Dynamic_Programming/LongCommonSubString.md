
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
