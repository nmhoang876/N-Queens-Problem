from SAT.binary import solve_n_queens_w_binary, print_solution
from SAT.commander import solve_n_queens_w_commander
from SAT.product import solve_n_queens_w_product
from SAT.sequential import solve_n_queens_w_sequential
from CP.CP_SAT import solve_n_queens_w_CP_SAT
from CP.Cplex_CP import solve_n_queens_w_Cplex
from ILP.Cplex_mip import solve_n_queens_w_cplex_mip
from ILP.Gurobi import solve_n_queens_w_gurobi

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
        solution = solve_n_queens_w_CP_SAT(n)

    elif s=="Cplex_CP":
        solution = solve_n_queens_w_Cplex(n)

    elif s=="Cplex_mip":
        solution = solve_n_queens_w_cplex_mip(n)

    elif s=="Gurobi":
        solution = solve_n_queens_w_gurobi(n)

    elif s=="Sequential":
        solution = solve_n_queens_w_sequential(n)

    else:
        print("Wrong input")

    print_solution(solution)
    print("Run time: %s seconds." %(time.time() - start_time))

if __name__ == "__main__":
    main()