from os.path import realpath, dirname
from pathlib import Path, PurePath

# Reference Outputs
# TODO Find/write lib for standardized output.

# -- Win Output --
# Real CWD at run: <path>\SubstanceHelpers
# Python CMD: python test\paths.py
#
# __file__: test\paths.py
# real: <path>\SubstanceHelpers\test\paths.py
# raw: <path>\SubstanceHelpers\test
# path: <path>\SubstanceHelpers\test
# name: test
# pure: <path>\SubstanceHelpers\test
# pureName: test

# -- Ubuntu (Win Bash) Home Output --
# Real CWD at run: <path>\SubstanceHelpers
# Python CMD: python test/paths.py
#
# __file__: test/paths.py
# real: SubstanceHelpers\test\paths.py
# raw: <path>\SubstanceHelpers\test
# path: <path>\SubstanceHelpers\test
# name: test
# path: <path>\SubstanceHelpers\test

# -- Ubuntu (Win Bash) Symlink Output --
# Real CWD at run: <path>\SubstanceHelpers
# Python CMD: python test/paths.py
#
# __file__: test/paths.py
# real: SubstanceHelpers\test\paths.py
# raw: <path>\SubstanceHelpers\test
# path: <path>\SubstanceHelpers\test
# name: test
# path: <path>\SubstanceHelpers\test

real = realpath(__file__)
raw = dirname(real)
path = Path(raw)
name = path.name
pure = PurePath(path)
pureName = pure.name
