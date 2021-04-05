class AdjNode:
    """
    A class to represent the adjacency list of the node
    """

    def __init__(self, data):
        """
        Constructor
        :param data : the next node.
        """
        self.node = data
        self.next = None


class Graph:
    """
    Graph Class Abstract Data Types
    """

    def __init__(self, vertices):
        """
        Constructor
        :param nodes : Total nodes in a graph
        """
        self.nodes = vertices
        self.graph = [None] * self.nodes

        # Function to add an edge in an undirected graph

    def add_edge(self, source, destination):
        """
        add edge
        :param source: Source node
        :param destination: Destination node
        """

        # Adding the node to the source node
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

    def print_graph(self):
        """
        A function to print a graph
        """
        for i in range(self.nodes):
            print("Adjacency list of node {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.node), end="")
                temp = temp.next
            print(" \n")


# Main program
if __name__ == "__main__":

    V = 5  # Total vertices
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()