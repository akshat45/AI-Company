from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _get_safe_path(file_path: str) -> Path:
    path = (PROJECT_ROOT / file_path).resolve()

    if not path.is_relative_to(PROJECT_ROOT):
        raise ValueError(
            "Access outside project directory is not allowed"
        )

    return path


def list_files(directory: str = ".") -> list[str]:
    """List files and directories inside the project directory."""

    path = _get_safe_path(directory)

    if not path.is_dir():
        raise ValueError(f"Not a directory: {directory}")

    return [
        str(item.relative_to(PROJECT_ROOT))
        for item in path.iterdir()
    ]


def read_file(file_path: str) -> str:
    """Read a text file from the project."""

    path = _get_safe_path(file_path)

    if not path.is_file():
        raise ValueError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")


def write_file(file_path: str, content: str) -> str:
    """Create or overwrite a text file inside the project."""

    path = _get_safe_path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        content,
        encoding="utf-8"
    )

    return f"File written successfully: {file_path}"