import sys

def greet_to_user(name):
    message = name + ", Hello"
    return message

def main():
    name = sys.argv[1]
    print(greet_to_user(name))

if __name__ == "__main__":
    main()
