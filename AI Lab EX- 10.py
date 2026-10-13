
import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

h = {'A': 5, 'B': 4, 'C': 2, 'D': 4,
     'E': 2, 'F': 1, 'G': 0}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            print("Path:", path)
            print("Total cost:", g)
            return

        if g > best_cost.get(node, float('inf')):
            continue

        for neighbor, cost in graph[node]:
            new_cost = g + cost

            if new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                heapq.heappush(
                    queue,
                    (new_cost + h[neighbor], new_cost,
                     neighbor, path + [neighbor])
                )

    print("Goal not found")

astar('A', 'G')
