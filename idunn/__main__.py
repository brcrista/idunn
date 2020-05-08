import sys

from idunn import idunn
from idunn.console import Console

usage = 'python -m idunn playlist-file.txt'

def main(args):
    console = Console()

    try:
        if len(args) != 2:
            print(f'Usage: {usage}')
            return 1

        idunn.run(input_file=args[1], console=console)
        return 0
    except Exception as ex:
        console.error(ex)
        return 2

if __name__ == '__main__':
    exit(main(sys.argv))