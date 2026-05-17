N = 4

board = [["." for _ in range(N)] for _ in range(N)]

col = [False] * N
diag1 = [False] * (2 * N)
diag2 = [False] * (2 * N)

def solve(row):
    if row == N:
        for r in board:
            print(" ".join(r))
        return True

    for c in range(N):

        if col[c] or diag1[row-c] or diag2[row+c]:
            continue

        # Place queen
        board[row][c] = "Q"
        col[c] = True
        diag1[row-c] = True
        diag2[row+c] = True

        if solve(row + 1):
            return True

        # Backtrack
        board[row][c] = "."
        col[c] = False
        diag1[row-c] = False
        diag2[row+c] = False

    return False

solve(0)
