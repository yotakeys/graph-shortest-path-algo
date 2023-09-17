class Graph():

    __max = 99999999
    __dist = []
    __sptSet = []
    __route = []

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.__dist = [self.__max] * vertices
        self.__sptSet = [False] * vertices
        self.__route = [-1] * vertices

    def printSolution(self):
        print("Vertex \t Distance from Source \t Route")
        for node in range(self.V):
            print(node, "\t\t", self.__dist[node], "\t\t", self.__route[node])

    def minDistance(self):

        min = self.__max

        for v in range(self.V):
            if self.__dist[v] < min and self.__sptSet[v] == False:
                min = self.__dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        self.__dist = [self.__max] * self.V
        self.__dist[src] = 0
        self.__sptSet = [False] * self.V

        for _ in range(self.V):

            u = self.minDistance()

            self.__sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   self.__sptSet[v] == False and
                   self.__dist[v] > self.__dist[u] + self.graph[u][v]):
                    self.__dist[v] = self.__dist[u] + self.graph[u][v]
                    self.__route[v] = u


if __name__ == "__main__":
    g = Graph(11)
    g.graph = [[0, 2, 8, 1, 0, 0, 0, 0, 0, 0, 0],
               [2, 0, 6, 0, 1, 0, 0, 0, 0, 0, 0],
               [8, 6, 0, 7, 5, 1, 2, 0, 0, 0, 0],
               [1, 0, 7, 0, 0, 0, 9, 0, 0, 0, 0],
               [0, 1, 5, 0, 0, 3, 0, 2, 9, 0, 0],
               [0, 0, 1, 0, 3, 0, 4, 0, 6, 0, 0],
               [0, 0, 2, 9, 0, 4, 0, 0, 3, 1, 0],
               [0, 0, 0, 0, 2, 0, 0, 0, 7, 0, 9],
               [0, 0, 0, 0, 9, 6, 3, 7, 0, 1, 2],
               [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 4],
               [0, 0, 0, 0, 0, 0, 0, 9, 2, 4, 0]
               ]
    g.dijkstra(0)
    g.printSolution()
