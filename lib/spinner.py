class Spinner:
    CHARS = '/-\\|'

    def __init__(self):
        self.pos = 0

    def __next__(self):
        import sys
        sys.stdout.write('{}\r'.format(self.CHARS[self.pos]))
        sys.stdout.flush()

        self.pos += 1
        self.pos %= len(self.CHARS)
