import os

def read_file(path):
    # BUG: no exception handling, file might not exist
    with open(path) as f:
        return f.read()

def write_file(path, content):
    # BUG: overwrites without warning
    with open(path, 'w') as f:
        f.write(content)

def list_files(directory):
    # BUG: no check if directory exists
    return os.listdir(directory)

def delete_file(path):
    # BUG: no check if file exists before deleting
    os.remove(path)
