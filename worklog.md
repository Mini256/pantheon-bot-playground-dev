# Worklog

## Phase 0 — Context verification

- Branch: `pantheon/fix-brokenpipeerror-202603020537`
- Issue location: `hello.py:9` contains `print(greet(name))`
- Repro (Linux):
  - `python3 hello.py world | head -n 0`
  - Observed: `BrokenPipeError` emitted during stdout finalization (`Exception ignored in: <_io.TextIOWrapper ...>`)
  - Exit code: `120` (from the `python3` side of the pipe)

## Phase 1 — Analysis & design

### Root cause analysis (RCA)

- When `stdout` is a pipe and the consumer exits early, writes to `stdout` fail with `EPIPE`, surfaced by Python as `BrokenPipeError`.
- The current script does not handle this exception. This can cause noisy stderr output and a non-zero exit status during interpreter shutdown/flush.

### Design

- Use a `try/except BrokenPipeError` around output in `main()`.
- On `BrokenPipeError`, exit gracefully with code `0` and redirect `stdout` to `os.devnull` via `os.dup2(...)` to prevent additional `BrokenPipeError` during shutdown flush.
- Keep normal behavior unchanged for interactive/non-piped usage.
- Add regression tests using `subprocess` to:
  - verify normal output/exit code
  - simulate a broken pipe by running `hello.py` with `stdout` connected to a pipe that has no reader, asserting exit code `0` and no traceback/noise on stderr.

## Phase 2 — Implementation & verification

- Implemented `BrokenPipeError` handling in `hello.py` by flushing output, catching `BrokenPipeError`, redirecting `stdout` to `os.devnull`, and exiting with code `0`.
- Added `unittest` coverage in `tests/test_hello.py` for normal output and broken-pipe behavior.
- Test run: `python3 -m unittest discover -v` (pass)
