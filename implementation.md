# CLI argument validation (`hello.py`)

## Problem
`hello.py` previously accessed `sys.argv[1]` without validating that a positional argument was provided. Running the script with no arguments raised `IndexError` and produced a traceback.

## Behavior
- With a name argument: `python3 hello.py Ada` prints `Hello, Ada` and exits `0`.
- With no arguments: `python3 hello.py` prints a usage message to **stderr** and exits `2` (usage error).

## Implementation
- `main()` now checks `len(sys.argv) < 2` before reading `sys.argv[1]`.
- On missing arguments, it prints `Usage: hello.py NAME` to `stderr` and calls `sys.exit(2)`.
- When an argument is present, the original greeting behavior is unchanged.

## Tests
Run the test suite from the repo root:

```bash
python3 -m unittest -v
```

