class SimpleCache:
    def __init__(self):
        self.data = {}

    def get(self, key):
        # BUG: KeyError if key not found
        return self.data[key]

    def set(self, key, value):
        self.data[key] = value

    def delete(self, key):
        # BUG: KeyError if key not found
        del self.data[key]
