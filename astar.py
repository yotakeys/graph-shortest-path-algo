import heapq


class Graph:

    graph = []
    __cost = int
    __path = []

    class Node:
        def __init__(self, state, cost, heuristic):
            self.state = state
            self.cost = cost
            self.heuristic = heuristic
            self.total_cost = cost + heuristic
            self.path = [state]

        def __lt__(self, other):
            return self.total_cost < other.total_cost

    def calculate_heuristic(self, node, goal):
        return goal - node

    def a_star(self, start, goal):
        open_set = []
        heapq.heappush(open_set, self.Node(
            start, 0, self.calculate_heuristic(start, goal)))

        visited = set()

        while open_set:
            current_node = heapq.heappop(open_set)

            if current_node.state == goal:
                self.__cost = current_node.cost
                self.__path = current_node.path

            visited.add(current_node.state)

            for neighbor, cost in enumerate(self.graph[current_node.state]):
                if cost == 0 or neighbor in visited:
                    continue

                total_cost = current_node.cost + cost
                heuristic = self.calculate_heuristic(neighbor, goal)
                new_node = self.Node(neighbor, total_cost, heuristic)
                new_node.path = current_node.path + [neighbor]

                for existing_node in open_set:
                    if existing_node.state == neighbor and existing_node.total_cost < new_node.total_cost:
                        break
                else:
                    heapq.heappush(open_set, new_node)

    def printSolution(self):
        print(f"Shortest path from {start_node} to {goal_node}: {self.__path}")
        print(f"Total cost: {self.__cost}")


if __name__ == '__main__':
    g = Graph()
    g.graph = [
        [0, 2, 8, 1, 0, 0, 0, 0, 0, 0, 0],
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

    start_node = 0
    goal_node = 10

    g.a_star(start_node, goal_node)
    g.printSolution()
