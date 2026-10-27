def minimax(depth, node, maximizing, values):
    if depth == 3:
        return values[node]

    if maximizing:
        return max(
            minimax(depth + 1, node * 2, False, values),
            minimax(depth + 1, node * 2 + 1, False, values)
        )
    else:
        return min(
            minimax(depth + 1, node * 2, True, values),
            minimax(depth + 1, node * 2 + 1, True, values)
        )

values = [3, 5, 2, 9, 12, 5, 23, 1]

result = minimax(0, 0, True, values)

print("Best value:", result)
