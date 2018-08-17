
## 一. 图论
  * [1. 定义](#1-定义)   
  * [2. 路径规划(最短路径问题 | 广度预优先优化)](#2-路径规划 | 最短路径问题 | 广度预优先优化)

### 1. 定义
图论可以看做字典，如：   
 graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}   
 ```
 # 找到一条从一点到另一点的路径
 def find_path(graph, start, end, path=[]):
        path = path + [start] # 加入开始节点
        if start == end:
            return path
        if not graph.get(start): # 若开始节点没有指向的点，说明不存在路径
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: 
                    return newpath
        return None
        
 # 找到所以的路径
  def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.get(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
        
 # 找到最短路径
  def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.get(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
 ```

### 2. 路径规划 | 最短路径问题 | 广度预优先优化

* 1. [小赛旅游](http://exercise.acmcoder.com/online/online_judge_ques?ques_id=2267&konwledgeId=139)

**题目描述**

小赛很想到外面的世界看看，于是收拾行装准备旅行。背了一个大竹筐，竹筐里装满了路上吃的，这些吃的够它走N公里。为了规划路线，它查看了地图，沿途中有若干个村庄，在这些村庄它都可以补充食物。但每次补充食物都需要花费时间，在它竹筐的食物足够可以走到下一个村庄的时候它就不用补充，这样背起来不累而且不花费时间。地图上可以看到村庄之间的距离，现在它要规划一下它的路线，确定在哪些村庄补充食物可以使沿途补充食物的次数最少。你能帮帮小赛吗？  
**要求：**   
  输入：  
      > 第一行有两个数字，第一个数字为竹筐装满可以走的公里数，即N值；第二个数字为起点到终点之间的村庄个数。  
      > 第二行为起点和村庄、村庄之间、村庄和终点之间的距离。且范围不能超过一个int型表达的范围。
      > 7 4    
      > 5  6  3  2  2   
  输出：   
      > 程序输出为至少需要补充食物的次数。   
      > 2

```
判断每段距离与装行李的重量N的大小，当dis[i]<N时，走不完该段路程；当N-dis[i] >= dis[i+1]即食物完全满足两段路的需求，将N-dis[i]重新赋给N继续走下
一段路；否则就没走一段路到达村庄后补给食物即装满N。
num = list(map(int, raw_input().split()))
dis = list(map(int, raw_input().split()))
N = num[0]
m = num[1]
count = 0
for i in range(m):
    if dis[i] > num[0]:
        break
    elif N - dis[i] >= dis[i+1]:
        N = N - dis[i]
    else:
        N = num[0]
        count += 1
print  count
```

二. 最短路径问题（图论广度优先搜索）

1. 走迷宫

https://github.com/ShaoQiBNU/mazes_BFS

https://github.com/BrickXu/subway   

**问题描述**

输入一组10 x 10的数据，由#和.组成的迷宫，其中#代表墙，.代表通路，入口在第一行第二列，出口在最后一行第九列，从任意一个.都能一步走到上下左右四个方向的.，请求出从入口到出口最短需要几步？   
输入示例：
```
#.########                                   #.########                     
#........#                                   #........#                      
#........#                                   ########.#
#........#                                   #........#
#........#                                   #.########
#........#                                   #........#
#........#                                   ########.#
#........#                                   #........#
#........#                                   #.######.#                                   
########.#                                   ########.#
结果为：16                                    结果为： 30

```

```
因为题意是使用最少的步数走出迷宫，所要可以使用广度优先遍历的方式，每处理完一层说明走了一步，最先到达出口使用的步数最少。

import  numpy as np
def bfs(N,maps,start,end):
    """
    1:已经访问；0: 每访问
    :param N: 矩阵大小
    :param maps: 矩阵
    :param start: 开始点
    :param end: 结束点
    :return: 步数
    """
    # 上下左右四个方向的增量
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    # 用于存放节点
    nodes = []
    # 开始的节点(x坐标，y坐标，步数)
    nodes.append((0,1,0))

    # 节点访问列表—记录节点是否被访问
    visitNodes = np.array([[0] * N] * N)
    visitNodes[0][1] = 1

    # bfs过程
    while len(nodes):
        # 上下左右四个方向遍历
        for i in range(4):
            # 从节点列表输出一个节点
            node = nodes[0]
            # 上下左右四个方向遍历
            x = node[0] + dx[i]
            y = node[1] + dy[i]
            # 步数
            step = node[2]
            # 判断是否到达终点
            if x ==9 and y == 8:
                return step+1
            # 判断节点是否符合条件
            if x>=1 and x<=9 and y>=1 and y<=9 and visitNodes[x][y] == 0 and maps[x][y] == 1:
                # 将节点压入节点列表nodes，说明进入下一层，step+1
                nodes.append((x,y,step+1))
                # 访问过该节点
                visitNodes[x][y] = 1
        # 从节点列表移除上一层的节点
        del nodes[0]
     # 没有路径无法走出时，返回0
    return  0



if __name__ == '__main__':
    maps1 = np.array([[0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
                       , [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
                       , [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
                       , [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
                       , [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 3, 0]])
    maps2 = np.array([[0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
                       , [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
                       , [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
                       , [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
                       , [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 3, 0]])

    res = bfs(10,maps2,2,3)
    print(res)

```

