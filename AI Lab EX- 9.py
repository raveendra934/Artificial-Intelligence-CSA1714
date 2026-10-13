
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
visited = [False] * n
path = [0]
visited[0] = True
cost = 0
current = 0

while len(path) < n:
    nearest = -1
    min_dist = float('inf')

    for city in range(n):
        if not visited[city] and dist[current][city] < min_dist:
            min_dist = dist[current][city]
            nearest = city

    path.append(nearest)
    visited[nearest] = True
    cost += min_dist
    current = nearest

cost += dist[current][0]
path.append(0)

print("Route:", path)
print("Total distance:", cost)
