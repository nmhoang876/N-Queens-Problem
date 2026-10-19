def solve_n_queens_w_CP_SAT(n):
    board = [[0 for j in range(n)] for i in range(n)]

    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            board[row][col] = 1
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if backtrack(row + 1):
                return True

            board[row][col] = 0
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return False

    if backtrack(0):
        return board
    else:
        return None