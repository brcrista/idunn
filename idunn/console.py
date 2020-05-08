import sys

import colorama

class Console:
    def __init__(self):
        colorama.init()

    def info(self, message):
        print(f'> {message}')

    def warning(self, message):
        print(f'{colorama.Fore.YELLOW}? {message}', file=sys.stderr)

    def error(self, message):
        print(f'{colorama.Fore.RED}! {message}', file=sys.stderr)