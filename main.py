from SAT.binary import solve_n_queens_w_binary, print_solution
from SAT.commander import solve_n_queens_w_commander
from SAT.product import solve_n_queens_w_product
from SAT.sequential import solve_n_queens_w_sequential
from CP.CP_SAT import solve_n_queens_ortools
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
        solution = solve_n_queens_ortools(n)

    else:
        solution = solve_n_queens_w_sequential(n)

    print_solution(solution)
    print("Run time: %s seconds." %(time.time() - start_time))

if __name__ == "__main__":
    main()