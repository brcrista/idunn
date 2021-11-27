import sys

from idunn import idunn
from idunn.console import Console

usage = 'python -m idunn playlist-file.txt [--yes]'

def main(args):
    console = Console()

    try:
        if len(args) < 2:
            print(f'Usage: {usage}')
            return 1

        yes = len(args) >= 3 and args[2] == '--yes'
        idunn.run(input_file=args[1], yes=yes, console=console)
        return 0
    except Exception as ex:
        console.error(ex)
        return 2

if __name__ == '__main__':
    exit(main(sys.argv))