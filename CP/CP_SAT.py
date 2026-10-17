from ortools.sat.python import cp_model

def solve_n_queens_ortools(n):
    # Khởi tạo mô hình CP
    model = cp_model.CpModel()

    # queens[i] là vị trí cột của quân hậu ở hàng i (giá trị từ 0 đến n-1)
    queens = [model.NewIntVar(0, n - 1, f'q_{i}') for i in range(n)]

    # 1. Các quân hậu không cùng cột
    model.AddAllDifferent(queens)

    # 2. Các quân hậu không cùng đường chéo chính (q_i + i phải khác nhau)
    model.AddAllDifferent([queens[i] + i for i in range(n)])

    # 3. Các quân hậu không cùng đường chéo phụ (q_i - i phải khác nhau)
    model.AddAllDifferent([queens[i] - i for i in range(n)])

    # Khởi tạo Solver
    solver = cp_model.CpSolver()
    # solver.parameters.max_time_in_seconds = 60.0 # Tùy chọn giới hạn thời gian

    # start_time = time.time()
    status = solver.Solve(model)
    # exec_time = time.time() - start_time

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        # Chuyển đổi lời giải về dạng ma trận bàn cờ 0/1
        board = [[0] * n for _ in range(n)]
        for i in range(n):
            col = solver.Value(queens[i])
            board[i][col] = 1
        return board
    else:
        return None
