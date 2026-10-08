from collections import deque

def valid(m, c):
    return (m == 0 or m >= c) and (m == 3 or 3-m >= 3-c)

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [start])])
    visited = {start}

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            for s in path:
                print(s)
            return

        for dm, dc in moves:
            if boat == 0:
                new_state = (m-dm, c-dc, 1)
            else:
                new_state = (m+dm, c+dc, 0)

            nm, nc, nb = new_state

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if valid(nm, nc) and valid(3-nm, 3-nc):
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [new_state]))

solve()
