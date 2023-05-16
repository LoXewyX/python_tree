# Interface
class TreeStructure:
    def __init__(self, space: str, branch: str, tee: str | list[str], last: str | list[str]):
        self.space = space
        self.branch = branch
        # [file, dir]
        self.tee = [tee, tee] if isinstance(tee, str) else tee[:2]
        self.last = [last, last] if isinstance(last, str) else last[:2]


# Presets
DEFAULT_STRUCTURE = TreeStructure(
    space='    ',
    branch='│   ',
    tee='├── ',
    last='└── '
)
DOUBLE_STRUCTURE = TreeStructure(
    space='    ',
    branch='║   ',
    tee='╠══ ',
    last='╠══ '
)
SHORT_STRUCTURE = TreeStructure(
    space='  ',
    branch='│ ',
    tee='├ ',
    last='└ '
)
ARROW_STRUCTURE = TreeStructure(
    space='    ',
    branch='│   ',
    tee='├─► ',
    last='└─► '
)
DISTRIBUTED_STRUCTURE = TreeStructure(
    space='    ',
    branch='│   ',
    tee=['├── ', '╞══ '],
    last=['└── ', '╘══ ']
)