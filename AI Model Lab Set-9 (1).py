
import heapq

goal = tuple(range(1, 16)) + (0,)

start = (
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 0,
    13, 14, 15, 12
)

def manhattan(state):
    distance = 0

    for i, value in enumerate(state):
        if value != 0:
            goal_pos = value - 1
            distance += abs(i // 4 - goal_pos // 4)
            distance += abs(i % 4 - goal_pos % 4)

    return distance

def get_neighbors(state):
    pos = state.index(0)
    row, col = divmod(pos, 4)
    moves = []

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        r, c = row + dr, col + dc

        if 0 <= r < 4 and 0 <= c < 4:
            new_pos = r * 4 + c
            temp = list(state)
            temp[pos], temp[new_pos] = temp[new_pos], temp[pos]
            moves.append(tuple(temp))

    return moves

def astar(start):
    pq = [(manhattan(start), 0, start)]
    visited = {start: None}
    cost = {start: 0}

    while pq:
        f, g, current = heapq.heappop(pq)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = visited[current]

            return path[::-1]

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in cost or new_g < cost[neighbor]:
                cost[neighbor] = new_g
                visited[neighbor] = current

                heapq.heappush(
                    pq,
                    (new_g + manhattan(neighbor),
                     new_g, neighbor)
                )

    return None

path = astar(start)

if path:
    print("Solution found!")
    print("Total Moves:", len(path) - 1)

    for state in path:
        for i in range(0, 16, 4):
            print(state[i:i+4])
        print()
else:
    print("No solution found")
