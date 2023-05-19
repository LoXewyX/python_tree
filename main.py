from os.path import isdir
from custom_pathlib import BuildDir
# from custom_pathlib.structure import DISTRIBUTED_STRUCTURE
from argparse import ArgumentParser

if __name__ == '__main__':
    # Define default values for arguments
    DEFAULT_LEVEL = -1
    DEFAULT_SHOW_ABS_PATH = 0
    DEFAULT_SHOW_SIZE = 0
    DEFAULT_PROPS = 'dfs'

    # Parse command-line arguments
    parser = ArgumentParser(description='Display a directory tree structure.')
    parser.add_argument('src', metavar='src', type=str, nargs='?', help='the path to the root directory of the tree structure to display')
    parser.add_argument('-l', '--level', metavar='level', type=int, default=DEFAULT_LEVEL,
                        help='the level of the tree structure to display (default: %(default)s)')
    parser.add_argument('-a', '--show_abs_path', metavar='show_abs_path', type=int, default=DEFAULT_SHOW_ABS_PATH,
                        help='whether or not to show the absolute path of each file and folder in the tree (default: %(default)s)')
    parser.add_argument('-s', '--show_size', metavar='show_size', type=int, default=DEFAULT_SHOW_SIZE,
                        help='whether or not to show the size of each file and folder in the tree (default: %(default)s)')
    parser.add_argument('-p', '--props', metavar='props', type=str, default=DEFAULT_PROPS,
                        help='the properties of each file and folder to display: [s] for max_size, [d] for directories and [f] for files (default: %(default)s)')

    args = parser.parse_args()

    path = args.src or ''

    while not isdir(path):
        path = input('Choose a valid directory: ')

    # Create BuildDir object and call bdir.tree with command-line arguments
    bdir = BuildDir(
        path=path,
        # struct=DISTRIBUTED_STRUCTURE
    )
    bdir.tree(
        level=args.level,
        show_abs_path=bool(args.show_abs_path),
        show_size=bool(args.show_size),
        props=args.props
    )
