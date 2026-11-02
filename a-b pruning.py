
import math

def print_board(board):
    for i in range(0, 9, 3):
        row = [
            board[j] if board[j] != "_" else "_"
            for j in range(i, i + 3)
        ]
        print(" ".join(row))
    print()


def check_winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] != "_":
            return board[a]

    if "_" not in board:
        return "Draw"

    return None


def alpha_beta(board, depth, alpha, beta, is_maximizing, nodes):
    nodes[0] += 1

    result = check_winner(board)

    if result == "X":
        return 1
    if result == "O":
        return -1
    if result == "Draw":
        return 0

    if is_maximizing:
        max_eval = -math.inf

        for i in range(9):
            if board[i] == "_":
                board[i] = "X"

                eval_score = alpha_beta(
                    board, depth + 1, alpha, beta, False, nodes
                )

                board[i] = "_"
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)

                if beta <= alpha:
                    break  # Beta cutoff

        return max_eval

    else:
        min_eval = math.inf

        for i in range(9):
            if board[i] == "_":
                board[i] = "O"

                eval_score = alpha_beta(
                    board, depth + 1, alpha, beta, True, nodes
                )

                board[i] = "_"
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)

                if beta <= alpha:
                    break  # Alpha cutoff

        return min_eval


def best_move(board):
    best_score = -math.inf
    move = -1
    nodes = [0]

    for i in range(9):
        if board[i] == "_":
            board[i] = "X"

            score = alpha_beta(
                board, 0, -math.inf, math.inf, False, nodes
            )

            board[i] = "_"

            if score > best_score:
                best_score = score
                move = i

    return move, nodes[0]



print("========== Alpha-Beta Pruning for Tic-Tac-Toe ==========")

board = ["_"] * 9

print("Initial Board:")
print_board(board)


move, nodes_evaluated = best_move(board)
board[move] = "X"

print(f"AI (X) chooses position {move}")
print(f"Nodes evaluated with Alpha-Beta: {nodes_evaluated}")
print("Board after AI move:")
print_board(board)


board[4] = "O"

print("Human (O) plays center (position 4)")
print_board(board)


move, nodes_evaluated = best_move(board)
board[move] = "X"

print(f"AI (X) chooses position {move}")
print(f"Nodes evaluated with Alpha-Beta: {nodes_evaluated}")
print("Board after AI move:")
print_board(board)
