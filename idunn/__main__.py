import sys

import idunn

usage = 'python -m idunn playlist-file.txt'

def main(args):
    try:
        if len(args) != 2:
            print(f'Usage: {usage}')
            return 1

        idunn.run(input_file=args[1])
        return 0
    except Exception as ex:
        print(ex, file=sys.stderr)
        return 2

if __name__ == '__main__':
    exit(main(sys.argv))