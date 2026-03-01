# CLI argument validation (`hello.py`)

## Summary
`hello.py` previously crashed with `IndexError` when run without a positional argument because it unconditionally accessed `sys.argv[1]`.

The fix adds a minimal guard in `main()`:
- If no `name` argument is provided, print a usage message to `stderr` and exit with code `2`.
- Otherwise, preserve existing behavior (print `Hello, <name>` to `stdout` and exit `0`).

## Usage
- `python3 hello.py Alice`
- `python3 hello.py` → prints `Usage: hello.py <name>` to `stderr`, exits `2`

## Tests
Run:
- `python3 -m unittest discover -s tests`

