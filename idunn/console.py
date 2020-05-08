import sys

class Console:
    def __init__(self):
        pass

    def info(self, message):
        print(f'> {message}')

    def warning(self, message):
        print(f'? {message}', file=sys.stderr)

    def error(self, message):
        print(f'! {message}', file=sys.stderr)