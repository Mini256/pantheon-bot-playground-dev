import sys

def greet_to_user(name):
    message = name + ", Hello"
    return message

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    print(greet_to_user(name))
    sys.exit(1)

if __name__ == "__main__":
    main()
