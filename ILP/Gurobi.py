def solve_n_queens_w_gurobi(n):
    x = [[-1 for j in range(n)] for i in range(n)]

    def is_valid(row, col):
        cnt = 0

        for j in range(n):
            if x[row][j] == 1:
                cnt += 1

        if cnt > 1:
            return False

        cnt = 0
        for i in range(n):
            if x[i][col] == 1:
                cnt += 1

        if cnt > 1:
            return False

        cnt = 0
        for i in range(n):
            for j in range(n):
                if i + j == row + col and x[i][j] == 1:
                    cnt += 1

        if cnt > 1:
            return False

        cnt = 0
        for i in range(n):
            for j in range(n):
                if i - j == row - col and x[i][j] == 1:
                    cnt += 1

        if cnt > 1:
            return False

        return True

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            for j in range(n):
                if j == col:
                    x[row][j] = 1
                else:
                    x[row][j] = 0

            if is_valid(row, col):
                if backtrack(row + 1):
                    return True

            for j in range(n):
                x[row][j] = -1

        return False

    if backtrack(0):
        return x
    else:
        return None