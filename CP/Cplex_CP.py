from docplex.cp.model import CpoModel

def solve_n_queens_cplex_cp(n):
    mdl = CpoModel(name="NQueens_CP")

    # Biến nguyên vị trí cột
    queens = [mdl.integer_var(0, n - 1, name=f"q_{i}") for i in range(n)]

    # Ràng buộc AllDifferent
    mdl.add(mdl.all_diff(queens))
    mdl.add(mdl.all_diff([queens[i] + i for i in range(n)]))
    mdl.add(mdl.all_diff([queens[i] - i for i in range(n)]))

    msol = mdl.solve(log_output=False)

    if msol:
        board = [[0] * n for _ in range(n)]
        for i in range(n):
            col = msol.get_value(queens[i])
            board[i][col] = 1
        return board
    else:
        return None
