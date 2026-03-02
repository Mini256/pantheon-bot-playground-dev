import os
import sys

def greet(name):
    message = "Hello, " + name
    return message

def main():
    name = sys.argv[1]
    try:
        print(greet(name))
        sys.stdout.flush()
    except BrokenPipeError:
        devnull_fd = None
        try:
            devnull_fd = os.open(os.devnull, os.O_WRONLY)
            os.dup2(devnull_fd, 1)
        except OSError:
            pass
        finally:
            if devnull_fd is not None:
                os.close(devnull_fd)
        sys.exit(0)

if __name__ == "__main__":
    main()
