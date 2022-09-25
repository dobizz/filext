from typing import Union


def get_bytes(file: Union[str, bytes]) -> bytes:
    if isinstance(file, str):
        with open(file, "rb") as fh:
            file_bytes = fh.read()
    elif isinstance(file, bytes):
        file_bytes = file
    else:
        raise TypeError
    return file_bytes


def validate_header(data: bytes, header: bytes, offset: int = 0) -> bool:
    return data[offset : len(header) + offset] == header


def validate_trailer(data: bytes, trailer: bytes, offset: int = 0) -> bool:
    length = len(data)
    return data[length - len(trailer) - offset : length - offset] == trailer
