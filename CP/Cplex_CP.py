def solve_n_queens_w_Cplex(n):
    initial_domains = {}

    for i in range(n):
        initial_domains[i] = set()

        for j in range(n):
            initial_domains[i].add(j)

    def assign(var, val, current_domains):
        new_domains = {}

        for i in current_domains:
            new_domains[i] = set(current_domains[i])

        new_domains[var] = {val}

        for i in range(n):
            if i == var:
                continue

            new_domains[i].discard(val)
            new_domains[i].discard(val + (i - var))
            new_domains[i].discard(val - (i - var))

            if len(new_domains[i]) == 0:
                return None

        return new_domains

    def select_unassigned_variable(assignment, current_domains):
        unassigned = []

        for i in range(n):
            if i not in assignment:
                unassigned.append(i)

        var = unassigned[0]

        for i in unassigned:
            if len(current_domains[i]) < len(current_domains[var]):
                var = i

        return var

    def backtrack(assignment, current_domains):
        if len(assignment) == n:
            return assignment

        var = select_unassigned_variable(assignment, current_domains)

        for val in current_domains[var]:
            new_domains = assign(var, val, current_domains)

            if new_domains is not None:
                assignment[var] = val

                result = backtrack(assignment, new_domains)

                if result is not None:
                    return result

                del assignment[var]

        return None

    assignment = backtrack({}, initial_domains)

    if assignment is not None:
        board = [[0 for j in range(n)] for i in range(n)]

        for r, c in assignment.items():
            board[r][c] = 1

        return board
    else:
        return None