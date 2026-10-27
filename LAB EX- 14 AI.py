def alphabeta(depth, node, alpha, beta, maximizing, values):
    if depth == 3:
        return values[node]

    if maximizing:
        best = -999

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i,
                              alpha, beta, False, values)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i,
                              alpha, beta, True, values)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 2, 9, 12, 5, 23, 1]

result = alphabeta(0, 0, -999, 999, True, values)

print("Best value:", result)
