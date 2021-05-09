# A simple graph representation and printing the adjacency matrix
class Graph:
    """ Class which represent the graph """
    def __init__(self, num_of_vertex):
        self.adj_matrix = [[-1] * num_of_vertex for i in range(num_of_vertex)]
        self.num_of_vertex = num_of_vertex
        self.vertices = {}
        self.vertices_list = [0] * num_of_vertex

    def get_adjacency_matrix(self):
        """ Method to print the ajancency matrix"""
        for row in self.adj_matrix:
            print(row)


    def set_vertex(self, vertex, identity):
        """ Method to set the vertex """
        if 0 <= vertex <= self.num_of_vertex:
            self.vertices[identity] = vertex
            self.vertices_list[vertex] = identity

    def set_edge(self, source, destination, weight = 0):
        """ Method to set the edge of the vertices """
        source_idx = self.vertices[source]
        destination_idx = self.vertices[destination]
        self.adj_matrix[source_idx][destination_idx] = weight
        self.adj_matrix[destination_idx][source_idx] = weight

    def get_edge(self):
        """ Get the edge and its weight """
        edge = []
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                if self.adj_matrix[i][j] != -1:
                    edge.append("{0}->{1}:{2}".format(self.vertices_list[i],\
                                                     self.vertices_list[j],\
                                                     self.adj_matrix[i][j]))
        return edge

if __name__ == "__main__":
    graph = Graph(5)
    graph.set_vertex(0,'0')
    graph.set_vertex(1,'1')
    graph.set_vertex(2,'2')
    graph.set_vertex(3,'3')
    graph.set_vertex(4,'4')
    #graph.set_vertex(5,'f')
    #graph.set_vertex(6,'g')
    
    graph.set_edge('0','1',20)
    graph.set_edge('0','4',10)
    graph.set_edge('1','0',30)
    graph.set_edge('1','2',70)
    graph.set_edge('1','3',50)
    graph.set_edge('1','4',79)
    graph.set_edge('2','1',79)
    graph.set_edge('2','3',45)
    graph.set_edge('3','1',45)
    graph.set_edge('3','2',23)
    graph.set_edge('3','4',42)
    graph.set_edge('4','0',45)
    graph.set_edge('4','1',45)
    graph.set_edge('4','3',45)

    graph.get_adjacency_matrix()

