class Graph:

    graph = []
    __dist = []

    def __init__(self, vertices):
        self.V = vertices
        self.__route = [[-1 for column in range(vertices)]
                        for row in range(vertices)]

    def floyd(self):
        self.__dist = self.graph

        for r in range(self.V):
            for p in range(self.V):
                for q in range(self.V):
                    if (self.__dist[p][r] + self.__dist[r][q] <= self.__dist[p][q]):
                        self.__dist[p][q] = self.__dist[p][r] + \
                            self.__dist[r][q]

    def printSolution(self):
        print("Distance : ")
        for p in range(self.V):
            for q in range(self.V):
                print(self.__dist[p][q], end="  ")
            print(" ")


if __name__ == "__main__":
    INF = 999
    g = Graph(11)

    g.graph = [[0, 2, 8, 1, INF, INF, INF, INF, INF, INF, INF],
               [2, INF, 6, INF, 1, INF, INF, INF, INF, INF, INF],
               [8, 6, INF, 7, 5, 1, 2, INF, INF, INF, INF],
               [1, INF, 7, INF, INF, INF, 9, INF, INF, INF, INF],
               [0, 1, 5, INF, INF, 3, INF, 2, 9, INF, INF],
               [0, INF, 1, INF, 3, INF, 4, INF, 6, INF, INF],
               [0, INF, 2, 9, INF, 4, INF, INF, 3, 1, INF],
               [0, INF, INF, INF, 2, INF, INF, INF, 7, INF, 9],
               [0, INF, INF, INF, 9, 6, 3, 7, INF, 1, 2],
               [0, INF, INF, INF, INF, INF, 1, INF, 1, INF, 4],
               [0, INF, INF, INF, INF, INF, INF, 9, 2, 4, INF]
               ]
    g.floyd()
    g.printSolution()
