class Graph:

    __max = 999999
    __route = []
    __dist = []

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.__route = [-1] * vertices
        self.__dist = [self.__max] * vertices

    def addEdge(self, a, b, c):
        self.graph.append([a, b, c])

    def printSolution(self):
        print("Vertex \t Distance from Source \t Route")
        for node in range(self.V):
            print(node, "\t\t", self.__dist[node], "\t\t", self.__route[node])

    def bellmanFord(self, src):

        self.__dist = [self.__max] * self.V
        self.__dist[src] = 0

        for _ in range(self.V - 1):
            for a, b, c in self.graph:
                if self.__dist[a] != self.__max and self.__dist[a] + c < self.__dist[b]:
                    self.__dist[b] = self.__dist[a] + c
                    self.__route[b] = a


if __name__ == "__main__":
    g = Graph(11)

    g.addEdge(0, 1, 2)
    g.addEdge(0, 2, 8)
    g.addEdge(0, 3, 1)

    g.addEdge(1, 0, 2)
    g.addEdge(1, 2, 6)
    g.addEdge(1, 4, 1)

    g.addEdge(2, 0, 8)
    g.addEdge(2, 1, 6)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 4, 5)
    g.addEdge(2, 5, 1)
    g.addEdge(2, 6, 2)

    g.addEdge(3, 0, 1)
    g.addEdge(3, 2, 7)
    g.addEdge(3, 6, 9)

    g.addEdge(4, 1, 1)
    g.addEdge(4, 2, 5)
    g.addEdge(4, 5, 3)
    g.addEdge(4, 7, 2)
    g.addEdge(4, 8, 9)

    g.addEdge(5, 2, 1)
    g.addEdge(5, 4, 3)
    g.addEdge(5, 6, 4)
    g.addEdge(5, 8, 6)

    g.addEdge(6, 2, 2)
    g.addEdge(6, 3, 9)
    g.addEdge(6, 5, 4)
    g.addEdge(6, 8, 3)
    g.addEdge(6, 9, 1)

    g.addEdge(7, 4, 2)
    g.addEdge(7, 8, 7)
    g.addEdge(7, 10, 9)

    g.addEdge(8, 4, 9)
    g.addEdge(8, 5, 6)
    g.addEdge(8, 6, 3)
    g.addEdge(8, 7, 7)
    g.addEdge(8, 9, 1)
    g.addEdge(8, 10, 2)

    g.addEdge(9, 6, 1)
    g.addEdge(9, 8, 1)
    g.addEdge(9, 10, 4)

    g.addEdge(10, 7, 9)
    g.addEdge(10, 9, 4)
    g.addEdge(10, 8, 2)

    g.bellmanFord(0)
    g.printSolution()
