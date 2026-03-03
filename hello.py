import sys

def greet_to_user(name):
    message = "Hello, " + name[:-1] + "!"
    return message

greet = greet_to_user

def main():
    name = sys.argv[1]
    print(greet_to_user(name))

if __name__ == "__main__":
    main()
