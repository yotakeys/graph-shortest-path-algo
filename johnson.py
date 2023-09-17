class Graph:

    __max = 999
    graph = []

    def __init__(self, vertices):
        self.V = vertices

    def minDistance(self, dist, visited):

        (minimum, minVertex) = (self.__max, 0)
        for vertex in range(len(dist)):
            if minimum > dist[vertex] and visited[vertex] == False:
                (minimum, minVertex) = (dist[vertex], vertex)

        return minVertex

    def Dijkstra(self, graph, modifiedGraph, src):

        sptSet = [False] * self.V
        dist = [self.__max] * self.V
        dist[src] = 0
        route = [-1] * self.V

        for c_ in range(self.V):

            curVertex = self.minDistance(dist, sptSet)
            sptSet[curVertex] = True

            for vertex in range(self.V):
                if ((sptSet[vertex] == False) and
                        (dist[vertex] > (dist[curVertex] +
                                         modifiedGraph[curVertex][vertex])) and
                        (graph[curVertex][vertex] != 0)):

                    dist[vertex] = (dist[curVertex] +
                                    modifiedGraph[curVertex][vertex])
                    route[vertex] = curVertex

        for vertex in range(self.V):
            print('Vertex ' + str(vertex) + ': ' +
                  str(dist[vertex]) + " soruce : " + str(route[vertex]))

    def BellmanFord(self, edges):

        dist = [self.__max] * (self.V + 1)
        dist[self.V] = 0
        edges = []

        for i in range(self.V):
            edges.append([self.V, i, 0])

        for i in range(self.V):
            for (src, des, weight) in edges:
                if ((dist[src] != self.__max) and
                        (dist[src] + weight < dist[des])):
                    dist[des] = dist[src] + weight

        return dist[0:self.V]

    def JohnsonAlgorithm(self):

        edges = []

        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):

                if self.graph[i][j] != 0:
                    edges.append([i, j, self.graph[i][j]])

        modifyWeights = self.BellmanFord(edges)

        modifiedGraph = [[0 for x in range(len(self.graph))] for y in
                         range(len(self.graph))]

        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):

                if self.graph[i][j] != 0:
                    modifiedGraph[i][j] = (self.graph[i][j] +
                                           modifyWeights[i] - modifyWeights[j])

        print('Modified Graph: ' + str(modifiedGraph))

        for src in range(len(self.graph)):
            print('\nShortest Distance with vertex ' +
                  str(src) + ' as the source:\n')
            self.Dijkstra(self.graph, modifiedGraph, src)


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

    g.JohnsonAlgorithm()
