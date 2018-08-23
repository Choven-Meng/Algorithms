**深度优先搜索**

&emsp;&emsp;简要来说dfs是对每一个可能的分支路径深入到不能再深入为止，而且每个节点只能访问一次。深度优先搜索的缺点也出来了：**难以寻找最优解**，仅仅只能寻找有解。其优点就是**内存消耗小**。

算法思想：

&emsp;&emsp;假设初始状态是图中所有顶点均未被访问，则从某个顶点v出发，首先访问该顶点，然后依次从它的各个未被访问的邻接点出发深度优先搜索遍历图，直至图中所有和v有路径相通的顶点都被访问到。 若此时尚有其他顶点未被访问到，则另选一个未被访问的顶点作起始点，重复上述过程，直至图中所有顶点都被访问到为止。   
显然，深度优先搜索是一个递归的过程。

**1. 无向图的深度优先搜索**

<img src="https://github.com/wangkuiwu/datastructs_and_algorithm/blob/master/pictures/graph/iterator/02.jpg?raw=true" alt="">  

对上面的图进行深度优先遍历，从顶点A开始。  

```
第1步：访问A。    
第2步：访问(A的邻接点)C。     
  在第1步访问A之后，接下来应该访问的是A的邻接点，即"C,D,F"中的一个。但在本文的实现中，顶点ABCDEFG是按照顺序存储，C在"D和F"的前面，因此，先访问C。   
第3步：访问(C的邻接点)B。    
  在第2步访问C之后，接下来应该访问C的邻接点，即"B和D"中一个(A已经被访问过，就不算在内)。而由于B在D之前，先访问B。    
第4步：访问(C的邻接点)D。    
  在第3步访问了C的邻接点B之后，B没有未被访问的邻接点；因此，返回到访问C的另一个邻接点D。    
第5步：访问(A的邻接点)F。    
  前面已经访问了A，并且访问完了"A的邻接点B的所有邻接点(包括递归的邻接点在内)"；因此，此时返回到访问A的另一个邻接点F。    
第6步：访问(F的邻接点)G。   
第7步：访问(G的邻接点)E。

因此访问顺序是：A -> C -> B -> D -> F -> G -> E
```

**2. 有向图的深度优先搜索**

<img src="https://github.com/wangkuiwu/datastructs_and_algorithm/blob/master/pictures/graph/iterator/04.jpg?raw=true" alt="">  
对上面的图进行深度优先遍历，从顶点A开始。   

```
第1步：访问A。 
第2步：访问B。 
    在访问了A之后，接下来应该访问的是A的出边的另一个顶点，即顶点B。 
第3步：访问C。 
    在访问了B之后，接下来应该访问的是B的出边的另一个顶点，即顶点C,E,F。在本文实现的图中，顶点ABCDEFG按照顺序存储，因此先访问C。 
第4步：访问E。 
    接下来访问C的出边的另一个顶点，即顶点E。 
第5步：访问D。 
    接下来访问E的出边的另一个顶点，即顶点B,D。顶点B已经被访问过，因此访问顶点D。 
第6步：访问F。 
    接下应该回溯"访问A的出边的另一个顶点F"。 
第7步：访问G。

因此访问顺序是：A -> B -> C -> E -> D -> F -> G
```

### 示例1. 城堡问题

**问题描述：**

```
     1   2   3   4   5   6   7  
   #############################
 1 #   |   #   |   #   |   |   #
   #####---#####---#---#####---#
 2 #   #   |   #   #   #   #   #
   #---#####---#####---#####---#
 3 #   |   |   #   #   #   #   #
   #---#########---#####---#---#
 4 #   #   |   |   |   |   #   #
   #############################
           (图 1)

   #  = Wall   
   |  = No wall
   -  = No wall

图1是一个城堡的地形图。请你编写一个程序，计算城堡一共有多少房间，最大的房间有多大。城堡被分割成mn(m≤50，n≤50)个方块，每个方块可以有0~4面墙。 
Input程序从标准输入设备读入数据。第一行是两个整数，分别是南北向、东西向的方块数。在接下来的输入行里，每个方块用一个数字(0≤p≤50)描述。用一个数字表示方块周围的墙，1表示西墙，2表示北墙，4表示东墙，8表示南墙。每个方块用代表其周围墙的数字之和表示。城堡的内墙被计算两次，方块(1,1)的南墙同时也是方块(2,1)的北墙。输入的数据保证城堡至少有两个房间。Output城堡的房间数、城堡中最大房间所包括的方块数。结果显示在标准输出设备上。 
Sample Input:
4  7 
11 6 11 6 3 10 6 
7 9 6 13 5 15 5 
1 10 12 7 13 7 5 
13 11 10 8 10 12 13 
Sample Output
5
9
```

<img src="//img-blog.csdn.net/20180316152743872?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L0xaSF8xMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="">   
<img src="//img-blog.csdn.net/20180316152812703?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L0xaSF8xMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="">  

<img src="//img-blog.csdn.net/20180316152908233?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L0xaSF8xMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="">  

```
rows, cols = map(int, input().split())
rooms = []
for i in range(rows):
    rooms.append(list(map(int, input().split())))

# 同一房间有相同的color值
color = [[0] * cols for _ in range(rows)]
roomNum = 0 # 房间数量
maxRoomArea = 0 # 房间的方块数

def DFS(i,j):
    global roomNum
    global roomArea
    if color[i][j]!=0:
        return
    roomArea += 1
    color[i][j] = roomNum
    # 向西走
    if rooms[i][j] & 1 == 0:
        DFS(i, j - 1)
    # 向北走
    if rooms[i][j] & 2 == 0:
        DFS(i - 1, j)
    # 向东走
    if rooms[i][j] & 4 == 0:
        DFS(i, j + 1)
    # 向南走
    if rooms[i][j] & 8 == 0:
        DFS(i + 1, j)

for i in range(rows):
    for j in range(cols):
        if color[i][j] == 0:
            roomNum += 1
            roomArea = 0
            DFS(i,j)
            maxRoomArea = max(roomArea,maxRoomArea)
print('房间数量:',roomNum)
print('最大房间的方块数：',maxRoomArea)
print(color)

#output
房间数量: 5
最大房间的方块数： 9
[[1, 1, 2, 2, 3, 3, 3], [1, 1, 1, 2, 3, 4, 3], [1, 1, 1, 5, 3, 5, 3], [1, 5, 5, 5, 5, 5, 3]]
```
