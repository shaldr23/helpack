# Tools for managing files path

from pathlib import Path


def abspath(rel_path):
    """
    Makes absolute path for path relative to script file
    """
    directory = Path(__file__).absolute()
    custom_abspath = Path.joinpath(directory, rel_path)
    return custom_abspath


if __name__ == '__main__':
    print(abspath('dir/prog'))
