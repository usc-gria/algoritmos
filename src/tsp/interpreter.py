"""Intérprete por lotes: liñas, comentarios, shlex e comandos."""
from __future__ import annotations
import argparse
from pathlib import Path
import shlex
import sys

# Permite tamén executar directamente este ficheiro.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tsp.commands import COMMANDS
from tsp.models import Solver


def main(solver_type: type[Solver] = Solver) -> None:
    parser = argparse.ArgumentParser(description="Intérprete de comandos TSP")
    parser.add_argument("file", help="Ficheiro UTF-8 de comandos, ou - para stdin")
    parser.add_argument("--time", action="store_true", help="Tempos en stderr")
    args = parser.parse_args()
    input_base = Path.cwd() if args.file == "-" else Path(args.file).resolve().parent
    problem = None
    line_number = 0
    stream = None
    try:
        stream = sys.stdin if args.file == "-" else Path(args.file).open(encoding="utf-8")
        for line_number, line in enumerate(stream, 1):
            clean = line.strip()
            if not clean or clean.startswith("#"):
                continue
            command, *arguments = shlex.split(clean)
            command = command.upper()
            if command == "LOAD" and arguments:
                arguments[0] = str(input_base / arguments[0])
            if command not in COMMANDS:
                raise ValueError("Unknown command")
            if command == "TSP":
                problem = COMMANDS[command](problem, *arguments,
                    solver_type=solver_type, timing=args.time)
            else:
                problem = COMMANDS[command](problem, *arguments)
    except (OSError, ValueError, TypeError, OverflowError, NotImplementedError) as exc:
        print(f"[LINE {line_number}] ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
    finally:
        if stream is not None and stream is not sys.stdin:
            stream.close()


if __name__ == "__main__":
    main()
