from pathlib import Path  # Not compatible with Python 2.7


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_source_root() -> Path:
    return Path(__file__).parent
