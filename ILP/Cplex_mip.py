def solve_n_queens_w_cplex_mip(n):
    board = [[0 for j in range(n)] for i in range(n)]

    def check_constraints(placement):
        rows = []
        cols = []
        diag1 = []
        diag2 = []

        for r, c in placement:
            rows.append(r)
            cols.append(c)
            diag1.append(r + c)
            diag2.append(r - c)

        if len(rows) != len(set(rows)):
            return False

        if len(cols) != len(set(cols)):
            return False

        if len(diag1) != len(set(diag1)):
            return False

        if len(diag2) != len(set(diag2)):
            return False

        return True

    def backtrack(row, placement):
        if row == n:
            return placement

        for col in range(n):
            new_placement = placement + [(row, col)]

            if check_constraints(new_placement):
                result = backtrack(row + 1, new_placement)

                if result is not None:
                    return result

        return None

    placement = backtrack(0, [])

    if placement is not None:
        for r, c in placement:
            board[r][c] = 1

        return board
    else:
        return None