from node import Node

class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    def add_edge(self,node1, node2, weight=0):

        if not node1 in self.adj_list.keys():
            return("this node does not exist")
        
        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def get_vertices(self):
        return(self.adj_list.keys())
    
    def get_neighbors(self,vertix):
        keys_list = self.adj_list.keys()
        
        for i in range (keys_list):
            if i == vertix:
                return self.adj_list[i]
        return "does not exist"
    def size(self):
        return len(self.adj_list.keys())

    # Code Challenge 36
    def breadth_frist(self,node):
        visited=[]
        explored=[]
        visited.append(node)
        explored.append(node)

        while explored:
            n=explored.pop()
            print(n, space=" ")
            
            for neighbours in self.adj_list[node.value]:
                if neighbours  not in visited:
                    visited.append(neighbours)
                    explored.append(neighbours)
    
    
# Code Challenge 38
    def depth_first(self, node):
        visited = []
        explored = []
        visited.append(node)
        explored.append(node)

        while explored:
            n = explored.pop()
            print(n, end=" ")

            for neighbour in self.adj_list[n.value]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    explored.append(neighbour)

    def exist(self,node1,node2):
        if node1 in self.adj_list[node2.value]:
            return True
        else:
            return False
    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output
        