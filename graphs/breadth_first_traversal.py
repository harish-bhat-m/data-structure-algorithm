""" Implmentation of breadth first traversal of the graph"""
from graph import Graph

class BFT():
    """ Implementation of breadth first traversal implementation"""

    def __init__(self, graph, source_node):
        self.graph = graph
        self.source_node = source_node

    def traversal(self):
        """
        Method  to breadth first traversal of graph
        :param None
        :return String of nodes
        """
        # Mark all the nodes as not visited
        visited = [False] * (len(self.graph.graph))

        # Creating the queue list
        queue = []

        # Adding the source node to the queue
        queue.append(self.source_node)

        # Marking the source node as visited
        visited[self.source_node] = True

        while queue:
            source = queue.pop(0)
            result = str(source)

            while self.graph.graph[source] is not None:
                data = self.graph.graph[source].node
                if not visited[data]:
                    queue.append(data)
                    visited[data] = True
                self.graph.graph[source] = self.graph.graph[source].next
        return result

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_graph()

bft = BFT(g,0)
traversed_string = bft.traversal()
print("Traversal")
print(traversalString)


