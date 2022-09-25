from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Dict, Union


def get_bytes(file: Union[str, bytes]) -> bytes:
    """
    Returns the raw bytes of a given file.

    Args:
        file (Union[str, bytes]): path to file or bytes of file

    Raises:
        TypeError: if file argument is not str or bytes

    Returns:
        bytes: bytes of file
    """
    if isinstance(file, str):
        with open(file, "rb") as fh:
            file_bytes = fh.read()
    elif isinstance(file, bytes):
        file_bytes = file
    else:
        raise TypeError
    return file_bytes


def validate_header(data: bytes, header: bytes, offset: int = 0) -> bool:
    """
    Validates file header by checking the header data from a given offset

    Args:
        data (bytes): bytes of file to check
        header (bytes): bytes of header
        offset (int, optional): byte offset position from start of file. Defaults to 0.

    Returns:
        bool: True if header is valid, else False if invalid
    """
    return data[offset : len(header) + offset] == header


def validate_trailer(data: bytes, trailer: bytes, offset: int = 0) -> bool:
    """
    Validates file trailer by checking the trailer from a given offset

    Args:
        data (bytes): bytes of file to check
        trailer (bytes): bytes of trailer
        offset (int, optional): byte offset position from end of file. Defaults to 0.

    Returns:
        bool: True if trailer is valid, else False if invalid
    """
    length = len(data)
    return data[length - len(trailer) - offset : length - offset] == trailer


def lookup_file_type(
    file: Union[str, bytes], file_types: Dict[str, Callable]
) -> Union[str, None]:
    """
    Does a parallel search from the given file types and returns the found file type.

    Args:
        file (Union[str, bytes]): path to file or bytes of file
        file_types (Dict[str, Callable]): dictionary of file types with the file type as the key and the classifier function as the value

    Returns:
        Union[str,None]: found file type or None
    """
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(checker, file): file_type
            for file_type, checker in file_types.items()
        }
        for future in as_completed(futures):
            result = futures[future]
            if future.result():
                return result
