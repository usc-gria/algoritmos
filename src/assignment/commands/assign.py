"""ASSIGN <TRIVIAL|PRECISE> <centro> [centro ...]."""
from __future__ import annotations
import json
import sys
from time import perf_counter
from ..models import Problem, Solver


def assign(problem: Problem | None, mode: str, first_center: str, *other_centers: str,
           solver_type: type[Solver] = Solver, timing: bool = False) -> Problem | None:
    mode = mode.upper()
    if mode not in ("TRIVIAL", "PRECISE"):
        raise ValueError("Expected TRIVIAL or PRECISE")
    centers = (first_center, *other_centers)
    if len(set(centers)) != len(centers):
        raise ValueError("Duplicate center")
    if problem is None:
        print("NO PROBLEM LOADED")
    elif not problem.names:
        print("PROBLEM IS EMPTY")
    elif missing := sorted(set(centers) - set(problem.names)):
        print(f"NODE {json.dumps(missing[0], ensure_ascii=False)} NOT PRESENT IN PROBLEM")
    else:
        solver = solver_type(problem, centers)
        start = perf_counter()
        cost, allocation, expanded = solver.solve(mode)
        elapsed = perf_counter() - start
        pairs = [[point, center] for point, center in zip(solver.points, allocation)]
        print(f"ASSIGN {mode}: {json.dumps(pairs, ensure_ascii=False)} WITH COST {cost}")
        print(f"EXPANDED {mode}: {expanded}", file=sys.stderr)
        if timing:
            print(f"TIME {mode}: {elapsed:.6f} s", file=sys.stderr)
    return problem
