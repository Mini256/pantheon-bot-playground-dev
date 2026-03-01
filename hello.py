import sys

def greet(name):
    message = "Hello, " + name
    return message

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} NAME", file=sys.stderr)
        sys.exit(2)
    name = sys.argv[1]
    print(greet(name))

if __name__ == "__main__":
    main()
