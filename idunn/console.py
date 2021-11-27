import sys

import colorama

class Console:
    """
    Interfaces with a user through the command line.
    """
    def __init__(self):
        colorama.init()

    def info(self, message):
        print(f'{colorama.Style.RESET_ALL}> {message}')

    def warning(self, message):
        print(f'{colorama.Fore.YELLOW}? {message}', file=sys.stderr)

    def error(self, message):
        print(f'{colorama.Fore.RED}! {message}', file=sys.stderr)

    def accept(self, prompt) -> bool:
        responses = ['y', 'n', '']
        while (response := input(f'{colorama.Style.RESET_ALL}> {prompt} [Y/n] ')).lower() not in responses:
            self.warning(f'Invalid choice: {response}')
        return response == '' or response.lower() == 'y'