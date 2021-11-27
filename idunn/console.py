import sys

import colorama

class Console:
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
        response = input(f'{colorama.Style.RESET_ALL}> {prompt} [Y/n] ').lower()
        while response not in responses:
            self.warning(f'Invalid choice: {response}')
            response = input(f'{colorama.Style.RESET_ALL}> {prompt} [Y/n] ').lower()

        return response == '' or response.lower() == 'y'