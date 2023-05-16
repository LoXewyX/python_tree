from os import sep
from pathlib import Path
from custom_pathlib.structure import TreeStructure, DEFAULT_STRUCTURE

# Classes
class BuildDir:
    def __init__(self, path: Path | str, struct: TreeStructure = DEFAULT_STRUCTURE):
        self._path = Path(path)
        self._space = struct.space
        self._branch = struct.branch
        self._tee_file = struct.tee[0]
        self._tee_dir = struct.tee[1]
        self._last_file = struct.last[0]
        self._last_dir = struct.last[1]

    # Getters
    @property
    def get_path(self) -> Path:
        return self._path

    # private functions
    def __format_size(self, size: int) -> str:
        units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
        for x in units:
            if size < 1024.0:
                return '%3.2f %s' % (size, x)
            size /= 1024.0


    # public functions
    def tree(self, level: int, show_abs_path: bool | None, show_size: bool, props: str) -> None:
        dir_path = self._path
        files = 0
        directories = 0
        sizes = 0

        def inner(dir_path: Path, level: int = -1, prefix: str = '', index: int = 0):
            nonlocal files, directories, sizes

            if level == 0:
                return

            contents = list(dir_path.iterdir())
            num_contents = len(contents)

            for i, path in enumerate(contents):
                if path.is_dir():
                    pointer = self._tee_dir if i < num_contents - 1 else self._last_dir
                    yield prefix+pointer+path.name+Path.sep
                    directories += 1
                    extension = self._branch if pointer == self._tee_dir else self._space
                    yield from inner(path, prefix=prefix+extension, level=level-1, index=i)
                else:
                    size = path.stat().st_size
                    pointer = self._tee_file if i < num_contents - 1 else self._last_file
                    yield prefix+pointer+path.name+(f' ({self.__format_size(size)})' if show_size else '')
                    files += 1
                    sizes += size

        if show_abs_path != None:
            print((str(dir_path.absolute()) if show_abs_path else dir_path.name) + sep)

        iterator = inner(dir_path, level=level)
        for line in iterator:
            print(line)

        if props != '':
            s = []
            for char in props:
                match(char):
                    case 'd':
                        s.append(f'{directories} directories')
                    case 'f':
                        s.append(f'{files} files')
                    case 's':
                        s.append(self.__format_size(sizes))

            print('\n' + ', '.join(s))
