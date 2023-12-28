import sys
from pathlib import Path
from pathvalidate import validate_filepath, ValidationError
from string import ascii_letters, digits


def check_filename(filename: str) -> bool:
    """
    Validate the provided filename and pass an OK if it's valid

    Parameters
    ----------
    filename: str
        The string to check against filesystem rules

    Returns
    -------
    bool
        Whether the filename is valid or not
    """

    # Check if the filename meets file-naming rules
    try:
        validate_filepath(filename, sys.platform)
    except ValidationError as ve:
        raise ve

    fp = Path(filename)

    # Check if the file is an mp3 flle
    if fp.suffix != ".mp3":
        raise FileTypeError(f"{fp.name} should be an mp3 file")

    # Finally, check if the filename exists
    if not fp.exists():
        raise FileNotFoundError(f"{fp.name} not found")

    return True


class FileTypeError(Exception):
    """
    Custom Error class to encapsulate the file-type error
    """

    def __init__(self, message) -> None:
        super().__init__(message)


class ModelSelectionError(Exception):
    """
    Custom Error class to represent selecting a non-existing model
    """

    def __init__(self, message) -> None:
        super().__init__(message)
