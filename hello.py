import sys
from pathlib import Path

def greet(name):
    message = "Hello, " + name
    return message

def main():
    if len(sys.argv) < 2:
        prog = Path(sys.argv[0]).name
        print(f"Usage: {prog} <name>", file=sys.stderr)
        sys.exit(2)
    name = sys.argv[1]
    print(greet(name))

if __name__ == "__main__":
    main()
