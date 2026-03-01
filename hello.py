import sys

def greet(name):
    message = "Hello, " + name
    return message

def main():
    name = sys.argv[1]
    print(greet(name))

if __name__ == "__main__":
    main()
