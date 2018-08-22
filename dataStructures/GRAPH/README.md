
图

**利用矩阵创建图：**

```
class Graph:

    def __init__(self, vertex):
        self.vertex = vertex # 顶点
        self.graph = [[0] * vertex for i in range(vertex) ] # 形成vertex * vertex 维向量

    def add_edge(self, u, v):
        # 对称矩阵
        self.graph[u - 1][v - 1] = 1 
        self.graph[v - 1][u - 1] = 1

    def show(self)：
        for i in self.graph:
            for j in i:
                print(j, end=' ')
            print(' ')
 if __name__ == '__main__':
    g = Graph(10)
    g.add_edge(1,4)
    g.add_edge(4,2)
    g.add_edge(4,5)
    g.add_edge(2,5)
    g.add_edge(5,3)
    g.show()  
    
# output:
0 0 0 1 0 0 0 0 0 0  
0 0 0 1 1 0 0 0 0 0  
0 0 0 0 1 0 0 0 0 0  
1 1 0 0 1 0 0 0 0 0  
0 1 1 1 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0
```

**利用列表创建图：**

```
class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] for i in range(vertex)] # vertex * 1 维列表

    def add_edge(self, u, v):
        self.graph[u - 1].append(v - 1)

    def show(self):
        for i in range(self.vertex):
            print('%d: '% (i + 1), end=' ')
            for j in self.graph[i]:
                print('%d-> '% (j + 1), end=' ')
            print(' ')

if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1,4)
    g.add_edge(4,2)
    g.add_edge(4,5)
    g.add_edge(2,5)
    g.add_edge(5,3)
    g.show()
    print(g.graph)
    
# output:
1:  1->  4->   
2:  1->  5->   
3:  1->   
4:  1->  2->  5->   
5:  1->  3->   
[[0, 3], [0, 4], [0], [0, 1, 4], [0, 2]]
```

**利用字典创建图：**

```
class Graph(object):
    def __init__(self):
        self.List = {}

    def add_edge(self, fromVertex, toVertex):
        # check if vertex is already present
        if fromVertex in self.List.keys():
            self.List[fromVertex].append(toVertex)
        else:
            self.List[fromVertex] = [toVertex]

    def printList(self):
        for i  in self.List:
            print((str(i) + '->'+' -> '.join([str(j) for j in self.List[i]])))

if __name__ == '__main__':
    g = Graph()
    g.add_edge(1,4)
    g.add_edge(4,2)
    g.add_edge(4,5)
    g.add_edge(2,5)
    g.add_edge(5,3)
    g.printList()
    print(g.List)
```
