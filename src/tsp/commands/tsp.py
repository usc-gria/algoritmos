"""TSP <orixe> <BRUTE_FORCE|DYNAMIC>: saída determinista do ciclo óptimo."""
from __future__ import annotations
import json
import sys
from time import perf_counter
from ..models import Problem, Solver


def tsp(problem: Problem | None, origin: str, mode: str, *,
        solver_type: type[Solver] = Solver, timing: bool = False) -> Problem | None:
    mode = mode.upper()
    if mode not in ("BRUTE_FORCE", "DYNAMIC"):
        raise ValueError("Expected BRUTE_FORCE or DYNAMIC")
    if problem is None:
        print("NO PROBLEM LOADED")
    elif not problem.names:
        print("PROBLEM IS EMPTY")
    elif origin not in problem.names:
        print(f"NODE {json.dumps(origin, ensure_ascii=False)} NOT PRESENT IN PROBLEM")
    else:
        solver = solver_type(problem)
        start = perf_counter()
        cost, route = (solver.brute_force(origin) if mode == "BRUTE_FORCE"
                       else solver.dynamic(origin))
        elapsed = perf_counter() - start
        print(f"TSP {mode}: {json.dumps(list(route), ensure_ascii=False)} WITH COST {cost}")
        if timing:
            print(f"TIME {mode}: {elapsed:.6f} s", file=sys.stderr)
    return problem
