from SAT.binary import solve_n_queens_w_binary, print_solution
from SAT.commander import solve_n_queens_w_commander
from SAT.product import solve_n_queens_w_product
from SAT.sequential import solve_n_queens_w_sequential
from CP.CP_SAT import backtracking_for_CP_SAT
import time


def main ():
    n = int (input())
    start_time = time.time()
    s = input()

    if s == "binary":
        solution = solve_n_queens_w_binary(n)

    elif s=="commander":
        solution = solve_n_queens_w_commander(n)

    elif s=="product":
        solution = solve_n_queens_w_product(n)

    elif s=="CP_SAT":
        solution = backtracking_for_CP_SAT(n)

    else:
        solution = solve_n_queens_w_sequential(n)

    print_solution(solution)
    print("Run time: %s seconds." %(time.time() - start_time))

if __name__ == "__main__":
    main()